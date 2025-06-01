import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService


class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_apply_product_filter(self):
        driver = self.driver

        try:
            # Wait for the "Brand A" checkbox to be present and click it
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='Brand A']/input"))
            )
            brand_a_checkbox.click()
            time.sleep(2)  # Allow the UI to update

            # Check the count of product cards displayed
            products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
            self.assertEqual(len(products), 1, "Expected 1 product after applying 'Brand A' filter.")

            # Uncheck the "Brand A" filter
            brand_a_checkbox.click()
            time.sleep(2)  # Allow the UI to update

            # Verify that the original number of product cards is restored
            products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
            self.assertEqual(len(products), 2, "Expected 2 products after removing 'Brand A' filter.")

            # Locate the price slider
            price_slider = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter input[type='range']"))
            )
            actions = ActionChains(driver)
            actions.click_and_hold(price_slider).move_by_offset(-50, 0).release().perform()

            time.sleep(2)  # Allow the UI to update

            # Verify that the product count changes after applying price filter
            products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
            self.assertEqual(len(products), 1, "Expected 1 product after applying price filter.")

        except Exception as e:
            self.fail(f"Test failed due to an unexpected exception: {e}")


if __name__ == "__main__":
    unittest.main()