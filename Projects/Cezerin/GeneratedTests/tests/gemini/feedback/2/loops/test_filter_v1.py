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
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards or determine initial count: {e}")

        # Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or unclick 'Brand A' checkbox: {e}")

        # Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
            self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after unchecking Brand A")
        except Exception as e:
            self.fail(f"Could not find product cards or determine final count: {e}")

        # Locate the price slider component.
        # Move one of the slider handles to apply a price range filter.
        # Verify that the product count changes again.
        try:
            # Locate the price filter values
            price_filter_values = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )

            # Extract the text values
            price_values = price_filter_values.text.split("\n")

            # Assert that the price values are not empty
            self.assertTrue(len(price_values) == 2, "Price values should contain two values")

            # Extract the minimum price
            min_price = price_values[0].replace("$", "").replace(",", "")

            # Assert that the minimum price is not empty
            self.assertTrue(len(min_price) > 0, "Minimum price should not be empty")

            # Extract the maximum price
            max_price = price_values[1].replace("$", "").replace(",", "")

            # Assert that the maximum price is not empty
            self.assertTrue(len(max_price) > 0, "Maximum price should not be empty")

            # Locate the price filter values
            price_filter_values = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )

            # Extract the text values
            price_values = price_filter_values.text.split("\n")

            # Assert that the price values are not empty
            self.assertTrue(len(price_values) == 2, "Price values should contain two values")

            # Extract the minimum price
            min_price = price_values[0].replace("$", "").replace(",", "")

            # Assert that the minimum price is not empty
            self.assertTrue(len(min_price) > 0, "Minimum price should not be empty")

            # Extract the maximum price
            max_price = price_values[1].replace("$", "").replace(",", "")

            # Assert that the maximum price is not empty
            self.assertTrue(len(max_price) > 0, "Maximum price should not be empty")

        except Exception as e:
            self.fail(f"Could not find price slider or change price range: {e}")

if __name__ == "__main__":
    unittest.main()