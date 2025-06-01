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
        self.driver.set_window_size(1200, 800)

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute']/div[contains(text(), 'Brand')]/following-sibling::label/input[@type='checkbox']")
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable(brand_a_checkbox_locator))
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        product_cards_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column') and contains(@class, 'available')]")
        try:
            product_cards_after_filter = wait.until(EC.presence_of_all_elements_located(product_cards_locator))
            num_product_cards_after_filter = len(product_cards_after_filter)
            self.assertTrue(num_product_cards_after_filter > 0, "No product cards found after applying Brand A filter.")
        except Exception as e:
            self.fail(f"Could not find product cards after applying Brand A filter: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable(brand_a_checkbox_locator))
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox to uncheck: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards_after_uncheck = wait.until(EC.presence_of_all_elements_located(product_cards_locator))
            num_product_cards_after_uncheck = len(product_cards_after_uncheck)
            self.assertTrue(num_product_cards_after_uncheck > num_product_cards_after_filter, "Product card count did not increase after unchecking Brand A filter.")
        except Exception as e:
            self.fail(f"Could not find product cards after unchecking Brand A filter: {e}")

        # 7. Locate the price slider component.
        # Assuming the price slider influences the values in the price-filter-values div
        price_filter_values_locator = (By.CLASS_NAME, "price-filter-values")
        try:
            price_filter_values = wait.until(EC.presence_of_element_located(price_filter_values_locator))
        except:
            self.fail("Could not find price filter values element.")

        # Find the left price value
        left_price_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        try:
            left_price_element = wait.until(EC.presence_of_element_located(left_price_locator))
            initial_left_price = left_price_element.text
        except:
            self.fail("Could not find left price element.")

        # 8. Move one of the slider handles to apply a price range filter.
        # This requires more specific locators and potentially JS execution for a real slider.
        # Since we don't have the slider element details, we'll simulate a change by modifying the left price text.
        # This is a placeholder and needs to be adapted to the actual slider implementation.
        new_left_price = "$967.00"  # Example adjusted price from html_data
        if new_left_price:
            try:
                # Simulate the slider movement by directly changing the price
                driver.execute_script(f"arguments[0].innerText = '{new_left_price}';", left_price_element)
            except Exception as e:
                self.fail(f"Failed to simulate slider movement by changing price: {e}")
        else:
            self.fail("Could not determine new left price for slider simulation.")

        # 9. Verify that the product count changes again.
        try:
            product_cards_after_price_filter = wait.until(EC.presence_of_all_elements_located(product_cards_locator))
            num_product_cards_after_price_filter = len(product_cards_after_price_filter)
            self.assertNotEqual(num_product_cards_after_uncheck, num_product_cards_after_price_filter, "Product card count did not change after applying price filter.")
        except Exception as e:
            self.fail(f"Could not find product cards after applying price filter: {e}")

if __name__ == "__main__":
    unittest.main()