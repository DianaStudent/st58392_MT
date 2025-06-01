from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Wait for and select the "Brand A" checkbox
        try:
            brand_a_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox' and contains(..,'Brand A')]]"))
            )
            brand_a_checkbox.click()
            time.sleep(2)  # Wait for the filter to be applied
        except:
            self.fail("Brand A checkbox not found or clickable.")

        # Assert that only one product is displayed
        products_after_brand_filter = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        self.assertEqual(len(products_after_brand_filter), 1, "Product count mismatch after applying Brand A filter.")

        # Uncheck the "Brand A" checkbox
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for the filter to be removed

        # Assert that two products are displayed again
        products_after_unchecking = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        self.assertEqual(len(products_after_unchecking), 2, "Product count mismatch after removing Brand A filter.")

        # Use the interactive price slider component to change price filtering
        try:
            # Example, assuming there's a method to adjust the slider
            price_slider = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .some-slider-class"))
            )
            # This part may require further implementation depending on the slider library used
            # Example: Adjust slider (pseudo-action)
            driver.execute_script("arguments[0].value = 967;", price_slider)
            price_slider.send_keys("\n")
            time.sleep(2)  # Wait for the filter to be applied
        except:
            self.fail("Price slider not found or non-functional.")

        # Assert that one product is displayed after changing the price filter
        products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        self.assertEqual(len(products_after_price_filter), 1, "Product count mismatch after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()