import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        product_cards_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div")
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards: {e}")

        # Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards: {e}")

        self.assertNotEqual(initial_product_count, final_product_count, "The product count must change after unchecking the filter.")

        # Locate the price slider component.
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        try:
            price_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
        except Exception as e:
            self.fail(f"Could not find price filter: {e}")

        # Move one of the slider handles to apply a price range filter.
        # Note: This requires more specific selectors and potentially JavaScript execution
        #       to interact with the slider handles correctly.  This is a placeholder.
        #       A more robust solution would involve finding the slider element, calculating
        #       the desired offset, and using ActionChains to move the slider handle.
        #       Due to the lack of precise slider handle selectors in the provided HTML,
        #       this part is omitted for now.

        # Verify that the product count changes again.
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            price_filtered_product_count = len(product_cards)
        except Exception as e:
            self.fail(f"Could not find product cards: {e}")

        self.assertNotEqual(final_product_count, price_filtered_product_count, "The product count must change after applying price filter.")

if __name__ == "__main__":
    unittest.main()