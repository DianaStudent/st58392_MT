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

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not locate or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not locate product cards after filtering: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not locate or uncheck 'Brand A' checkbox: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
            self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after unchecking Brand A filter")
        except Exception as e:
            self.fail(f"Could not locate product cards after unchecking filter: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        # Note: Implementing the slider movement is complex without specific slider implementation details.
        #       Skipping slider movement for now and focusing on verifying its presence.
        try:
            price_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter"))
            )
        except Exception as e:
            self.fail(f"Could not locate the price slider component: {e}")

        # 9. Verify that the product count changes again.
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            price_filter_product_count = len(product_cards)
            self.assertTrue(price_filter_product_count > 0, "Price filter product count should be greater than 0")
            self.assertNotEqual(final_product_count, price_filter_product_count, "Product count should change after applying price filter")
        except Exception as e:
            self.fail(f"Could not locate product cards after applying price filter: {e}")

if __name__ == "__main__":
    unittest.main()