import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BookSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_search_and_filter_books(self):
        driver = self.driver
        wait = self.wait

        # Step 2. Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found.")
        search_link.click()

        # Step 3. Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input not found.")
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        if not search_button.is_displayed():
            self.fail("Search button not found or not visible.")
        search_button.click()

        # Step 4. Wait for the search results to load
        results_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
        if not results_container:
            self.fail("Products container not found.")

        # Step 5. Locate and interact with the price range slider
        # Assuming that the slider is operable programmatically to mimic user action
        price_slider_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slider-handle.min-slider-handle")))
        price_slider_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slider-handle.max-slider-handle")))
        if not price_slider_from or not price_slider_to:
            self.fail("Price slider handles not found.")

        ActionChains(driver).drag_and_drop_by_offset(price_slider_to, -50, 0).perform()  # Dummy values for demonstration

        # After slider adjustment, confirm the results update
        # Waiting for the products grid to update after slider movement
        filtered_products = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item-box")))
        if not filtered_products:
            self.fail("No products found in filtered results.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()