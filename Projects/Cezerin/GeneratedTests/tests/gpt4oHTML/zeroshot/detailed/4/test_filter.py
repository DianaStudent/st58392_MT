import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestFilterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("file:///path_to_your_local_file.html")  # Load your local HTML file
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter(self):
        driver = self.driver
        wait = self.wait

        # Wait for products and filters to be fully loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products")))

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[input[@type='checkbox'] and contains(text(),'Brand A')]")))
        if not brand_a_checkbox:
            self.fail("Brand A checkbox not found.")
        brand_a_checkbox.click()

        time.sleep(2)  # Wait 2 seconds
        brand_a_selected = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        initial_count = len(brand_a_selected)
        self.assertGreater(initial_count, 0, "No product visible after filtering by Brand A.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        time.sleep(2)  # Wait 2 seconds
        brand_a_unselected = driver.find_elements(By.CSS_SELECTOR, ".products .available.empty")
        self.assertGreater(len(brand_a_unselected), initial_count, "Products not restored after unchecking Brand A.")

        # Locate the price slider and reduce the maximum price to 1159
        price_slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values")))
        if not price_slider:
            self.fail("Price slider not found.")
        
        slider_handle = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='range']")))
        action = ActionChains(driver)
        move_by_offset = -50  # Approximate value depending on initial and target positions
        action.click_and_hold(slider_handle).move_by_offset(move_by_offset).release().perform()

        time.sleep(2)  # Wait for price filtering to take effect

        # Verify that the number of product cards is reduced
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .available:not(.empty)")
        self.assertGreater(initial_count, len(filtered_products), "Number of products did not reduce after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()