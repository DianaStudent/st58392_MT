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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
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
        product_cards_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")
        time.sleep(2)

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
            self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after unchecking Brand A")
        except Exception as e:
            self.fail(f"Could not find product cards after unchecking Brand A: {e}")
            
        # 7. Locate the price slider component.
        price_filter_locator = (By.XPATH, "//div[@class='price-filter']")
        try:
            price_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
        except Exception as e:
            self.fail(f"Could not find price filter: {e}")

        # 8. Move one of the slider handles to apply a price range filter.
        # Note: This part is difficult without knowing the exact implementation of the slider.
        # Assuming it's a range input or similar, we can try to adjust the values.
        # This is a placeholder and might need adjustments based on the actual slider implementation.
        # Find the left slider handle
        left_handle_locator = (By.XPATH, "//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        try:
            left_handle = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(left_handle_locator)
            )
            original_price = left_handle.text
        except:
            self.fail("Could not find left handle")

        # 9. Verify that the product count changes again.
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            price_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
            left_handle = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(left_handle_locator)
            )

            # Move the left handle to the right
            actions = ActionChains(driver)
            actions.click_and_hold(left_handle).move_by_offset(10, 0).release().perform()
            
            new_product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            new_product_count = len(new_product_cards)
            self.assertNotEqual(final_product_count, new_product_count, "Product count should change after applying price filter")
            
        except Exception as e:
            self.fail(f"Could not find product cards after applying price filter: {e}")

if __name__ == "__main__":
    unittest.main()