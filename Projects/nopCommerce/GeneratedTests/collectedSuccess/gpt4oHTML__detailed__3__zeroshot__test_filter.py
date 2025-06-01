import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver and open the browser
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

    def test_search_and_filter_by_price(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get('http://max/')

        # Step 2: Click on the "Search" link
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except:
            self.fail("Search link not found or not clickable.")

        # Step 3: Enter "book" in the search field and submit the search
        try:
            search_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_field.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()
        except:
            self.fail("Unable to perform search for 'book'.")

        # Step 4: Wait for the search results to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "products-container"))
            )
        except:
            self.fail("Search results did not load.")

        # Step 5: Adjust the price range slider to 0-25
        try:
            price_slider = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-range-filter"))
            )
            slider_from = price_slider.find_element(By.CLASS_NAME, "from")
            slider_to = price_slider.find_element(By.CLASS_NAME, "to")

            # Use ActionChains to simulate slider drag
            action = ActionChains(driver)

            # Move both ends of the slider to set the range to 0-25
            action.drag_and_drop_by_offset(slider_from, -10, 0).perform()  # Adjust as needed to reach 0
            action.drag_and_drop_by_offset(slider_to, -50, 0).perform()   # Adjust as needed to reach 25

            # Wait for the filtering to apply and the grid to update
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "item-grid"))
            )
        except:
            self.fail("Unable to adjust slider or update results.")

        # Step 6: Confirm at least one product is shown in the filtered results
        try:
            products = driver.find_elements(By.CLASS_NAME, "product-item")
            if not products or len(products) == 0:
                self.fail("No products found after applying filter.")
        except:
            self.fail("Product grid verification failed after filtering.")

if __name__ == "__main__":
    unittest.main()