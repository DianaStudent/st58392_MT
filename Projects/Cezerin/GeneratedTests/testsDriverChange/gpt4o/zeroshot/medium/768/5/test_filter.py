from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_apply_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Brand A']/input")))
        if not brand_a_checkbox:
            self.fail("Brand A checkbox is missing.")
        brand_a_checkbox.click()
        time.sleep(2)
        
        # Verify the number of displayed product cards changes (2 → 1)
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
        if not product_cards:
            self.fail("Product cards are missing.")
        self.assertEqual(len(product_cards), 1, "The number of displayed products should be 1 after filter.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify the original number of product cards is restored (1 → 2)
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
        if not product_cards:
            self.fail("Product cards are missing after unchecking the filter.")
        self.assertEqual(len(product_cards), 2, "The number of displayed products should be 2 after removing filter.")

        # Locate the price slider component and apply a price range filter
        price_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .column.has-text-left")))
        if not price_slider:
            self.fail("Price slider is missing.")
        
        # Assuming the slider can be moved via a script or simulated drag-and-drop; using keys for simplicity
        price_slider_text = price_slider.text
        price_filter_end = driver.find_element(By.CSS_SELECTOR, ".price-filter .column.has-text-right")
        driver.execute_script("arguments[0].innerText = '$967.00';", price_filter_end)
        time.sleep(2)

        # Verify the product count changes (2 → 1)
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
        if not product_cards:
            self.fail("Product cards are missing after applying price filter.")
        self.assertEqual(len(product_cards), 1, "The number of displayed products should be 1 after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()