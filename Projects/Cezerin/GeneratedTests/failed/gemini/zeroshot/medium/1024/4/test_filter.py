import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        # 1. Open the category page.
        # Already done in setUp

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards_after_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            initial_product_count = len(product_cards_after_filter)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards after filtering: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox to uncheck: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)
        try:
            product_cards_after_unfilter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            restored_product_count = len(product_cards_after_unfilter)
            self.assertTrue(restored_product_count > 0, "Restored product count should be greater than 0")
            self.assertNotEqual(initial_product_count, restored_product_count, "Product count should change after unfiltering")
        except Exception as e:
            self.fail(f"Could not find product cards after unfiltering: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        # 9. Verify that the product count changes again.
        try:
            # Locate the price filter values container
            price_filter_values = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )
            # Find the left price value element
            left_price_value = price_filter_values.find_element(By.CLASS_NAME, "has-text-left")
            # Get the initial left price
            initial_left_price = left_price_value.text

            # Locate the attribute filter
            attribute_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "attribute-filter"))
            )
            # Find the price filter
            price_filter = attribute_filter.find_element(By.XPATH, "//div[@class='attribute-title'][text()='Price']/ancestor::div[@class='price-filter']")

            # Find the price filter values
            price_filter_values = price_filter.find_element(By.CLASS_NAME, "price-filter-values")
            # Find the left price
            left_price = price_filter_values.find_element(By.CLASS_NAME, "has-text-left")
            # Get the initial left price
            initial_left_price = left_price.text

            # Find the product cards after price filtering
            product_cards_after_price_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            price_filtered_product_count = len(product_cards_after_price_filter)

            self.assertNotEqual(restored_product_count, price_filtered_product_count, "Product count should change after price filtering")

        except Exception as e:
            self.fail(f"Could not find or interact with price slider: {e}")

if __name__ == "__main__":
    unittest.main()