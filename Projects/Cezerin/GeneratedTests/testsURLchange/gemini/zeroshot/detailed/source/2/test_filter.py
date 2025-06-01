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
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(1200, 800)
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # 1. Open the category page - Done in setUp

        # 2. Wait until products and filters are fully loaded.
        product_locator = (By.CSS_SELECTOR, ".products .column a")
        self.wait.until(EC.presence_of_element_located(product_locator))

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']")
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()

        # 4. Confirm it is checked.
        brand_a_checked_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[contains(@class, 'attribute-checked')][text()='Brand A']/input[@type='checkbox']")
        self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards_locator = (By.CSS_SELECTOR, ".products .column a")
        product_cards = self.driver.find_elements(*product_cards_locator)
        self.assertEqual(len(product_cards), 1, "Product count should be 1 after filtering by Brand A.")

        # 6. Uncheck the filter and confirm product count is restored (e.g., 1 -> 2).
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))
        brand_a_checkbox.click()
        time.sleep(2)
        product_cards = self.driver.find_elements(*product_cards_locator)
        self.assertEqual(len(product_cards), 2, "Product count should be 2 after unchecking Brand A.")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159 .
        price_filter_values_locator = (By.CSS_SELECTOR, ".price-filter-values")
        price_filter_values = self.wait.until(EC.presence_of_element_located(price_filter_values_locator))
        if not price_filter_values:
            self.fail("Price filter values not found.")

        # Locate the right slider handle
        right_slider_handle_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        right_slider_handle = self.wait.until(EC.presence_of_element_located(right_slider_handle_locator))

        # Move the right slider handle to reduce the maximum price to 1159
        actions = ActionChains(self.driver)
        actions.click_and_hold(right_slider_handle).move_by_offset(-10, 0).release().perform()

        # 8. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards = self.driver.find_elements(*product_cards_locator)
        self.assertEqual(len(product_cards), 1, "Product count should be 1 after filtering by price.")

if __name__ == "__main__":
    unittest.main()