import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()

    def test_apply_filters(self):
        driver = self.driver
        wait = self.wait
        
        # Locate and apply "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label/input[@type='checkbox' and following-sibling::text()='Brand A']")))
        if not brand_a_checkbox:
            self.fail("Brand A checkbox not found.")
        
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # Verify the product count changes from 2 to 1
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Expected 1 product after applying Brand A filter.")
        
        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # Verify the product count changes from 1 to 2
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 2, "Expected 2 products after removing Brand A filter.")

        # Locate the price slider and adjust it
        price_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .column.has-text-left")))
        if not price_slider:
            self.fail("Price slider not found.")
        
        # Assuming there's a slider, perform click and drag actions
        slider_handle = driver.find_element(By.XPATH, "//div[@class='price-filter']//div[contains(@class, 'column has-text-left')]//div[contains(@class, 'noUi-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(slider_handle, 10, 0).perform()
        time.sleep(2)  # Wait for UI to update
        
        # Verify the product count changes again
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertLess(len(products), 2, "Expected product count less than 2 after applying price filter.")

if __name__ == "__main__":
    unittest.main()