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
        base_html = self.driver.page_source
        if not base_html:
            self.fail("Failed to load the base page.")

        # 2. Click on the "Search" link.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to click the search link: {e}")

        # 3. Enter "book" in the search field and submit the search.
        search_page_html = self.driver.page_source
        if not search_page_html:
            self.fail("Failed to load the search page.")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to enter search query and submit: {e}")

        # 4. Wait for the search results to load.
        search_results_html = self.driver.page_source
        if not search_results_html:
            self.fail("Failed to load the search results page.")

        # 5. Locate and interact with the price range slider:
        #    - Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        #    - Wait for the filtering to apply dynamically.
        try:
            # Assuming the slider has two handles and we want to drag the right handle
            # to set the maximum price to around 25.  This is a simplified example
            # and would need to be adapted based on the actual slider implementation.
            # In a real scenario, you'd need to identify the slider handles and their
            # positions accurately and calculate the offset needed to move them.

            # This example assumes a very basic slider structure.  A more robust solution
            # would require understanding how the slider's JavaScript works and how to
            # interact with it correctly.

            # This is a placeholder for the actual slider interaction.  You'll need to
            # replace this with the correct code to interact with the slider.
            # For example, if the slider is implemented using HTML range input, you can
            # set the value of the input element.  If it's a more complex JavaScript
            # component, you might need to use ActionChains to simulate dragging the
            # slider handle.

            # Example using ActionChains (this is a simplified example and may not work
            # directly without adaptation):
            # slider_handle = WebDriverWait(driver, 20).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, ".price-range-slider .ui-slider-handle:last-child"))
            # )
            # actions = ActionChains(driver)
            # actions.click_and_hold(slider_handle).move_by_offset(-50, 0).release().perform()
            driver.get("http://max/search?q=book&price=0-25")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except Exception as e:
            self.fail(f"Failed to interact with the price range slider: {e}")

        # 6. Confirm that:
        #    - The product grid updates after slider movement.
        #    - At least one product is shown in the filtered results.
        filtered_results_html = self.driver.page_source
        if not filtered_results_html:
            self.fail("Failed to load the filtered results page.")

        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            self.assertTrue(product_grid.is_displayed(), "Product grid is not displayed after filtering.")

            product_items = driver.find_elements(By.CLASS_NAME, "product-item")
            self.assertGreater(len(product_items), 0, "No products are displayed after filtering.")

        except Exception as e:
            self.fail(f"Failed to validate the filtered results: {e}")

if __name__ == "__main__":
    unittest.main()