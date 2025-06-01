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
        initial_html = driver.page_source
        if not initial_html:
            self.fail("Initial HTML is empty")

        # 1. Get initial product count
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products > div"))
        )
        initial_product_count = len(products)
        if initial_product_count == 0:
            self.fail("Initial product count is zero.")

        # 2. Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes.
        products_after_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products > div"))
        )
        filtered_product_count = len(products_after_filter)
        if filtered_product_count == 0:
            self.fail("Filtered product count is zero.")
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering.")

        # 5. Uncheck the "Brand A" filter.
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # 6. Verify that the original number of product cards is restored.
        products_after_uncheck = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products > div"))
        )
        uncheck_product_count = len(products_after_uncheck)
        self.assertEqual(initial_product_count, uncheck_product_count, "Product count was not restored after unchecking filter.")

        # 7. Locate the price slider component.
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        price_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )

        # Locate the left slider handle
        left_handle_locator = (By.XPATH, "//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        left_handle = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(left_handle_locator)
        )

        # Get the current text of the left handle
        initial_price_text = left_handle.text
        if not initial_price_text:
            self.fail("Initial price text is empty")

        # Move the left slider handle to apply a price range filter.
        action = ActionChains(driver)
        action.move_to_element(price_filter).click_and_hold(left_handle).move_by_offset(20, 0).release().perform()

        # 8. Verify that the product count changes again.
        products_after_price_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products > div"))
        )
        price_filtered_product_count = len(products_after_price_filter)
        self.assertNotEqual(uncheck_product_count, price_filtered_product_count, "Product count did not change after price filtering.")

if __name__ == "__main__":
    unittest.main()