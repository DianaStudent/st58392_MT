from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Locate and click on the "Brand A" checkbox
        try:
            brand_a_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Brand A')]/input"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to click on 'Brand A' checkbox: {e}")

        # Wait for products to be filtered
        time.sleep(2)

        # Check the number of visible product cards
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 1, "Product count should be 1 after applying 'Brand A' filter.")

        # Uncheck the "Brand A" filter
        try:
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to uncheck 'Brand A' checkbox: {e}")

        # Wait for products to be unfiltered
        time.sleep(2)

        # Check the number of visible product cards after removing the filter
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 2, "Product count should be 2 after removing 'Brand A' filter.")

        # Adjust the price filter slider
        try:
            price_slider = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']"))
            )
            # Simulate price slider interaction - this is a placeholder as actual slider interaction requires JS
            driver.execute_script("arguments[0].style.left = '30%';", price_slider)
        except Exception as e:
            self.fail(f"Failed to interact with the price slider: {e}")

        # Wait for price filter to apply
        time.sleep(2)

        # Check the number of visible product cards after applying price filter
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 1, "Product count should be 1 after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()