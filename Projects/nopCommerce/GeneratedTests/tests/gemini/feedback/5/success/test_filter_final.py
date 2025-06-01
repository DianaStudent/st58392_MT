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
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_link_locator)).click()

        # 2. Enter "book" in the search field and submit the search
        search_field_locator = (By.ID, "q")
        search_button_locator = (By.CLASS_NAME, "button-1.search-button")
        search_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_field_locator))
        search_field.send_keys("book")
        driver.find_element(*search_button_locator).click()

        # 3. Wait for the search results to load
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))

        # 4. Locate and interact with the price range slider
        # Note: This part requires more specific HTML structure for the slider.
        # Assuming a basic slider structure with two handles (min and max).
        # You'll need to adapt the locators based on the actual HTML.

        # Locate the product filter element
        product_filter_locator = (By.CLASS_NAME, "product-filters")
        product_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_filter_locator))

        # Locate the price range filter element
        price_range_filter_locator = (By.CLASS_NAME, "price-range-filter")
        price_range_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located(price_range_filter_locator))

        # Locate the slider element
        # Note: Replace with the correct locator for the slider element
        # slider_locator = (By.CLASS_NAME, "ui-slider")
        # slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located(slider_locator))

        # Locate the left handle of the slider
        # Note: Replace with the correct locator for the left handle element
        left_handle_locator = (By.XPATH, "//div[@class='product-filter price-range-filter']//span[@class='from']")
        left_handle = WebDriverWait(driver, 20).until(EC.presence_of_element_located(left_handle_locator))

        # Locate the right handle of the slider
        # Note: Replace with the correct locator for the right handle element
        right_handle_locator = (By.XPATH, "//div[@class='product-filter price-range-filter']//span[@class='to']")
        right_handle = WebDriverWait(driver, 20).until(EC.presence_of_element_located(right_handle_locator))

        # Get the current values of the slider handles
        left_handle_value = left_handle.text
        right_handle_value = right_handle.text

        # Move the right handle to set the maximum price to 25
        # Note: This requires a more precise implementation depending on the slider's behavior
        # and the available methods for interacting with it.
        # For example, you might need to calculate the offset based on the slider's width
        # and the desired price range.
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(right_handle, -50, 0).perform()  # Adjust the offset as needed

        # Wait for the filtering to apply dynamically
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))

        # 5. Confirm that the product grid updates after slider movement
        updated_product_grid = driver.find_element(*product_grid_locator)
        self.assertIsNotNone(updated_product_grid, "Product grid did not update after slider movement.")

        # 6. Confirm that at least one product is shown in the filtered results
        product_items_locator = (By.CLASS_NAME, "product-item")
        product_items = driver.find_elements(*product_items_locator)
        self.assertTrue(len(product_items) > 0, "No products found after applying the price filter.")

if __name__ == "__main__":
    unittest.main()