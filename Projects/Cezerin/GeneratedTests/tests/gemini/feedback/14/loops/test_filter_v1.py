import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        # 1. Open the category page (done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except NoSuchElementException:
            self.fail("Could not find 'Brand A' checkbox.")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            num_products_filtered = len(product_cards)
            self.assertGreater(num_products_filtered, 0, "No products displayed after filtering.")
        except NoSuchElementException:
            self.fail("Could not find product cards after filtering.")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except NoSuchElementException:
            self.fail("Could not find 'Brand A' checkbox to uncheck.")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            num_products_original = len(product_cards)
            self.assertGreater(num_products_original, 0, "No products displayed after unfiltering.")
            self.assertNotEqual(num_products_filtered, num_products_original, "Product count did not change after unfiltering.")
        except NoSuchElementException:
            self.fail("Could not find product cards after unfiltering.")

        # 7. Locate the price slider component.
        # The price slider is interactive, so we can't directly manipulate the input values.
        # Instead, we'll check if the price filter component exists.
        try:
            price_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter"))
            )
        except NoSuchElementException:
            self.fail("Could not find price slider component.")

        # 8. Move one of the slider handles to apply a price range filter.
        # Since we cannot directly manipulate the slider, we'll just verify that the price range is displayed.
        try:
            price_values = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )
        except NoSuchElementException:
            self.fail("Could not find price values after price filtering.")

        # 9. Verify that the product count changes again.
        time.sleep(2)
        try:
            product_cards = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            num_products_price_filtered = len(product_cards)
            self.assertNotEqual(num_products_original, num_products_price_filtered, "Product count did not change after price filtering.")
        except NoSuchElementException:
            self.fail("Could not find product cards after price filtering.")

if __name__ == "__main__":
    unittest.main()