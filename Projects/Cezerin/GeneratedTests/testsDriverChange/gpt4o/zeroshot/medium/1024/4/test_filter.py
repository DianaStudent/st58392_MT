from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Apply "Brand A" filter
        wait = WebDriverWait(driver, 20)

        brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Brand A']/input")))
        self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox is not present")
        brand_a_checkbox.click()

        # Wait for the UI to update
        time.sleep(2)

        # Check that the number of displayed product cards has changed
        displayed_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        self.assertEqual(len(displayed_products), 1, "Expected 1 product displayed after filter")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        # Wait for the UI to update
        time.sleep(2)

        # Verify that the original number of product cards is restored
        displayed_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        self.assertEqual(len(displayed_products), 2, "Expected 2 products displayed after removing filter")

        # Locate the price slider component and filter by price range
        price_slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']")))
        self.assertIsNotNone(price_slider, "Price filter slider is not present")

        # Assuming we drag the slider, for simplicity, we'll simulate this with a click interaction
        # This should ideally be replaced with action chains to drag the slider handle
        price_slider = driver.find_element(By.XPATH, "//div[@class='price-filter']//div[contains(@class, 'column')]")
        driver.execute_script("arguments[0].click();", price_slider)

        # Wait for the UI to update
        time.sleep(2)

        # Verify the product count changes again
        displayed_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        self.assertEqual(len(displayed_products), 1, "Expected 1 product displayed after price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()