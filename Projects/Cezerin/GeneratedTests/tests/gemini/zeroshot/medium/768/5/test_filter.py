import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_brand_filter(self):
        # 1. Open the category page - done in setUp

        # 2. Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        product_cards_locator = (By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards: {e}")

        # Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox to uncheck: {e}")

        # Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards after unchecking Brand A: {e}")

        self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after filtering")

        # Locate the price slider component.
        price_slider_locator = (By.XPATH, "//div[@class='price-filter']")
        try:
            price_slider = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(price_slider_locator)
            )
        except Exception as e:
            self.fail(f"Could not find price slider: {e}")

        # Move one of the slider handles to apply a price range filter.
        try:
            # Locate the left slider handle
            left_handle_locator = (By.XPATH, "//div[@class='columns is-mobile is-gapless price-filter-values']/div[1]")
            left_handle = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(left_handle_locator)
            )

            # Move the left handle
            actions = ActionChains(self.driver)
            actions.move_to_element(left_handle).click_and_hold(left_handle).move_by_offset(10, 0).release().perform()

        except Exception as e:
            self.fail(f"Could not move price slider handle: {e}")

        # Verify that the product count changes again.
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(product_cards_locator)
            )
            price_filtered_product_count = len(product_cards)
        except:
            self.fail("Could not find product cards after price filtering")

        self.assertNotEqual(final_product_count, price_filtered_product_count, "Product count should change after price filtering")

if __name__ == "__main__":
    unittest.main()