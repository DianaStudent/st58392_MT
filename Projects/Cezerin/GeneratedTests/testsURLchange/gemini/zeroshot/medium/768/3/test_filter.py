import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Failed to locate product cards or get initial count: {e}")

        # Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate or click 'Brand A' checkbox to uncheck: {e}")

        # Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            final_product_count = len(product_cards)

            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
            self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after unchecking the filter")

        except Exception as e:
            self.fail(f"Failed to locate product cards or get final count: {e}")

        # Locate the price slider component.
        try:
            price_filter_locator = (By.XPATH, "//div[@class='price-filter']")
            price_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
        except Exception as e:
            self.fail(f"Failed to locate price filter: {e}")

        # Move one of the slider handles to apply a price range filter.
        try:
            # Locate the left slider handle
            left_handle_locator = (By.XPATH, "//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
            left_handle = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(left_handle_locator)
            )

            # Move the left handle
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(left_handle, 20, 0).perform()

        except Exception as e:
            self.fail(f"Failed to interact with price slider: {e}")

        # Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # Verify that the product count changes again.
        try:
            product_cards_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            price_filtered_product_count = len(product_cards)
            self.assertTrue(price_filtered_product_count >= 0, "Price filtered product count should be greater than or equal to 0")
            self.assertNotEqual(final_product_count, price_filtered_product_count, "Product count should change after price filtering")

        except Exception as e:
            self.fail(f"Failed to locate product cards or get price filtered count: {e}")

if __name__ == "__main__":
    unittest.main()