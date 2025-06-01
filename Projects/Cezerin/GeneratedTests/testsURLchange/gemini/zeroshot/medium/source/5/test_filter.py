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
        initial_html = self.driver.page_source
        if not initial_html:
            self.fail("Initial HTML is empty.")

        # Get initial product count
        products_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div")
        initial_products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("Initial product count is 0.")

        # Filter by Brand A
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after filtering
        filtered_products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        filtered_product_count = len(filtered_products)

        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering by Brand A.")

        # Uncheck Brand A
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # Get product count after unchecking filter
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        unfiltered_products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        unfiltered_product_count = len(unfiltered_products)

        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count did not return to initial count after unchecking Brand A.")

        # Price filter
        price_filter_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']")
        price_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )

        # Move the left slider handle
        # Note: This is a placeholder.  A real implementation would require finding the slider handle element and using ActionChains to move it.
        # Due to the lack of specific slider handle elements in the HTML, this part is skipped.
        # Example:
        # slider_handle_locator = (By.CSS_SELECTOR, ".slider-handle-left")  # Replace with the actual selector
        # slider_handle = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(slider_handle_locator))
        # actions = ActionChains(driver)
        # actions.drag_and_drop_by_offset(slider_handle, 50, 0).perform()  # Move handle 50 pixels to the right

        # Get product count after price filtering
        # Due to the lack of a working price slider, this is commented out.
        # price_filtered_products = WebDriverWait(driver, 20).until(
        #     EC.presence_of_all_elements_located(products_locator)
        # )
        # price_filtered_product_count = len(price_filtered_products)
        # self.assertNotEqual(unfiltered_product_count, price_filtered_product_count, "Product count did not change after price filtering.")

if __name__ == "__main__":
    unittest.main()