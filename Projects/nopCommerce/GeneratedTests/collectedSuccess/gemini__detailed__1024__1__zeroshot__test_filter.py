import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click on the "Search" link
        search_link_locator = (By.LINK_TEXT, "Search")
        try:
            search_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_link_locator))
            search_link.click()
        except:
            self.fail("Search link not found")

        # 2. Enter "book" in the search field and submit the search
        search_field_locator = (By.ID, "q")
        search_button_locator = (By.CLASS_NAME, "button-1.search-button")
        try:
            search_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_field_locator))
            search_field.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_button_locator))
            search_button.click()
        except:
            self.fail("Search field or button not found")

        # 3. Wait for the search results to load
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))
        except:
            self.fail("Product grid did not load")

        # 4. Locate and interact with the price range slider
        # This requires more specific locators for the slider handles, which are not provided in the HTML.
        # Assuming there are elements that represent the slider handles, we would interact with them using ActionChains.
        # For example (this is a placeholder and needs to be adapted to the actual HTML):
        # slider_handle_min_locator = (By.CSS_SELECTOR, ".price-range-slider .handle.min")
        # slider_handle_max_locator = (By.CSS_SELECTOR, ".price-range-slider .handle.max")
        #
        # try:
        #     slider_handle_min = WebDriverWait(driver, 20).until(EC.presence_of_element_located(slider_handle_min_locator))
        #     slider_handle_max = WebDriverWait(driver, 20).until(EC.presence_of_element_located(slider_handle_max_locator))
        #
        #     # Move the slider handles to set the desired price range (e.g., 0-25)
        #     actions = ActionChains(driver)
        #     actions.drag_and_drop_by_offset(slider_handle_min, 5, 0).perform() # Move min handle
        #     actions.drag_and_drop_by_offset(slider_handle_max, -5, 0).perform() # Move max handle
        #
        #     # Wait for the filtering to apply dynamically
        #     WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))
        #
        # except:
        #     self.fail("Slider handles not found or interaction failed")

        # 5. Confirm that the product grid updates after slider movement and at least one product is shown in the filtered results.
        # Since slider interaction is not fully implemented due to missing HTML elements, we will check for the product grid and at least one product.
        try:
            product_grid = WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))
            product_items_locator = (By.CLASS_NAME, "product-item")
            product_items = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(product_items_locator))

            if not product_items:
                self.fail("No products found after filtering")

        except:
            self.fail("Product grid not found or no products displayed.")

if __name__ == "__main__":
    unittest.main()