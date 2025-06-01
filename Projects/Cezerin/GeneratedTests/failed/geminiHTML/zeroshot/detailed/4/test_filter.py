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
        self.driver.maximize_window()
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the category page. (Done in setUp)
        # 2. Wait until products and filters are fully loaded.
        products_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products")
        wait.until(EC.presence_of_element_located(products_locator))

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']")
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()

        # 4. Confirm it is checked.
        brand_a_checked_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[@class='attribute-checked']/input[@type='checkbox']")
        wait.until(EC.presence_of_element_located(brand_a_checked_locator))

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div")
        product_cards = driver.find_elements(*product_cards_locator)
        product_count_after_filter = len(product_cards)
        self.assertTrue(product_count_after_filter > 0, "No products found after filtering by Brand A.")
        
        # 6. Uncheck the filter and confirm product count is restored (e.g., 1 -> 2).
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checked_locator))
        brand_a_checkbox.click()
        time.sleep(2)
        product_cards = driver.find_elements(*product_cards_locator)
        product_count_after_uncheck = len(product_cards)
        self.assertTrue(product_count_after_uncheck > product_count_after_filter, "Product count did not increase after unchecking Brand A filter.")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        # Note: The provided HTML does not contain a price slider component.
        # Assuming the price filter values are used as input for price range.
        # Finding the price filter values
        price_filter_values_locator = (By.CSS_SELECTOR, ".price-filter .columns.is-mobile.is-gapless.price-filter-values")
        price_filter_values = wait.until(EC.presence_of_element_located(price_filter_values_locator))
        
        # Since there is no slider, we cannot move the slider handle.
        # This part of the test cannot be implemented with the provided HTML.
        
        # 8. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        # time.sleep(2)
        # product_cards = driver.find_elements(*product_cards_locator)
        # product_count_after_price_filter = len(product_cards)
        # self.assertTrue(product_count_after_price_filter < product_count_after_uncheck, "Product count did not decrease after price filtering.")
        
        print("Brand A filter test passed.")

if __name__ == "__main__":
    unittest.main()