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
        self.driver.get('http://localhost:3000/category-a')

    def test_filter_brand_and_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Checking "Brand A"
        try:
            brand_a_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Brand A')]/input"))
            )
            brand_a_checkbox.click()
            time.sleep(2)  # Waiting for UI update
        except Exception as e:
            self.fail("Could not find or interact with the 'Brand A' checkbox: " + str(e))

        # Verify number of products displayed is 1 after applying filter
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
            self.assertEqual(len(products), 1, "Expected 1 product to be visible after filtering by Brand A")
        except Exception as e:
            self.fail("Failed to count products after applying brand filter: " + str(e))

        # Unchecking "Brand A"
        try:
            brand_a_checkbox.click()
            time.sleep(2)  # Waiting for UI update
        except Exception as e:
            self.fail("Could not uncheck the 'Brand A' checkbox: " + str(e))

        # Verify number of products displayed is 2 after removing filter
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
            self.assertEqual(len(products), 2, "Expected 2 products to be visible after removing brand filter")
        except Exception as e:
            self.fail("Failed to count products after removing brand filter: " + str(e))

        # Adjust price range slider - assuming there's a price filter slider
        try:
            price_slider = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='range']"))
            )
            driver.execute_script("arguments[0].setAttribute('value', '967')", price_slider)
            time.sleep(2)  # Waiting for UI update
        except Exception as e:
            self.fail("Could not interact with the price slider: " + str(e))

        # Verify number of products displayed after changing price filter
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .column.available")
            self.assertEqual(len(products), 1, "Expected 1 product to be visible after adjusting price filter")
        except Exception as e:
            self.fail("Failed to count products after changing price filter: " + str(e))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()