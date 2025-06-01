from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Please replace with your actual URL

    def test_search_and_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page
        # Check if the search link exists
        search_link = wait.until(element_to_be_clickable((By.XPATH, "//a[@href='/search']")))
        if not search_link:
            self.fail("Search link not found.")

        # 2. Click on the "Search" link
        search_link.click()

        # 3. Enter "book" in the search field and submit the search
        search_input = wait.until(element_to_be_clickable((By.NAME, "q")))
        if not search_input:
            self.fail("Search input field not found.")
        
        search_input.send_keys("book")
        search_button = wait.until(element_to_be_clickable((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 4. Wait for the search results to load
        wait.until(presence_of_element_located((By.CLASS_NAME, "products-container")))

        # 5. Locate and interact with the price range slider
        # Assuming slider is present on page as shown in html_data examples
        slider_min = wait.until(presence_of_element_located((By.CLASS_NAME, "from")))
        slider_max = wait.until(presence_of_element_located((By.CLASS_NAME, "to")))
        
        if not slider_min or not slider_max:
            self.fail("Price range slider not found.")

        # Adjust the minimum or maximum range to 0-25 using ActionChains
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(slider_min, 10, 0).perform()  # Adjust based on actual slider behavior
        action.drag_and_drop_by_offset(slider_max, -10, 0).perform()  # Adjust based on actual slider behavior
        
        # 6. Confirm product grid updates after slider movement
        # Wait for at least one product to display in filtered results
        updated_products = wait.until(presence_of_element_located((By.CLASS_NAME, "product-item")))
        if not updated_products:
            self.fail("Filtered products not displaying after slider adjustment.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()