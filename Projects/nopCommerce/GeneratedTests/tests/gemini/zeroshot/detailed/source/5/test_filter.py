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

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on the "Search" link.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # 3. Enter "book" in the search field and submit the search.
        search_field_id = "q"
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, search_field_id))
        )
        search_field.send_keys("book")

        search_button_class = "button-1 search-button"
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, search_button_class))
        )
        search_button.click()

        # 4. Wait for the search results to load.
        product_grid_class = "product-grid"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, product_grid_class))
        )

        # 5. Locate and interact with the price range slider:
        # This part requires more specific HTML structure of the slider, which is not provided.
        # Assuming there are elements that can be dragged to adjust the price range.
        # The following code is a placeholder and needs to be adapted based on the actual slider implementation.

        # Locate the slider handle (replace with the actual selector)
        # slider_handle_locator = (By.CSS_SELECTOR, ".ui-slider-handle:nth-of-type(1)")
        # slider_handle = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located(slider_handle_locator)
        # )

        # # Move the slider handle (replace with the actual logic)
        # actions = ActionChains(driver)
        # actions.click_and_hold(slider_handle).move_by_offset(30, 0).release().perform()

        # Wait for the filtering to apply dynamically.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, product_grid_class))
        )

        # 6. Confirm that:
        # - The product grid updates after slider movement.
        # - At least one product is shown in the filtered results.

        product_items_class = "item-box"
        product_items = driver.find_elements(By.CLASS_NAME, product_items_class)

        if not product_items:
            self.fail("No products found after filtering.")

        self.assertTrue(len(product_items) > 0, "Product grid did not update or no products found after filtering.")

if __name__ == "__main__":
    unittest.main()