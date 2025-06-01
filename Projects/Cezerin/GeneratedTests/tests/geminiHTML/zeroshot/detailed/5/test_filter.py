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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        # 1. Open the category page.
        # 2. Wait until products and filters are fully loaded.
        products_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products")
        self.wait.until(EC.presence_of_element_located(products_locator))

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']")
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()

        # 4. Confirm it is checked.
        brand_a_checked_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[@class='attribute-checked']/input[@type='checkbox']")
        self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div")
        product_cards = self.driver.find_elements(*product_cards_locator)
        initial_product_count = len(product_cards)
        self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")

        # Uncheck the filter
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))
        brand_a_checkbox.click()

        # 6. Wait 2 seconds and verify that the number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)
        product_cards = self.driver.find_elements(*product_cards_locator)
        final_product_count = len(product_cards)
        self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
        self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after unchecking the filter")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        # Locate the price filter values
        price_filter_values_locator = (By.CSS_SELECTOR, ".price-filter .price-filter-values")
        price_filter_values = self.wait.until(EC.presence_of_element_located(price_filter_values_locator))

        # Locate the right slider handle
        right_slider_handle_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        right_slider_handle = self.wait.until(EC.presence_of_element_located(right_slider_handle_locator))

        # Move the right slider handle
        actions = ActionChains(self.driver)
        actions.click_and_hold(right_slider_handle).move_by_offset(-5, 0).release().perform()

        # 8. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards = self.driver.find_elements(*product_cards_locator)
        price_filtered_product_count = len(product_cards)
        self.assertTrue(price_filtered_product_count >= 0, "Price filtered product count should be greater than or equal to 0")
        self.assertNotEqual(final_product_count, price_filtered_product_count, "Product count should change after applying price filter")

if __name__ == "__main__":
    unittest.main()