import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAutomationUI(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header:
            self.fail("Header is not found or not visible.")
        
        # Check for footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer:
            self.fail("Footer is not found or not visible.")

        # Check for navigation menu
        top_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
        if not top_menu:
            self.fail("Navigation menu is not found or not visible.")
        
        # Check for search box elements
        search_form = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        if not search_form:
            self.fail("Search form is not found or not visible.")

        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        if not search_input:
            self.fail("Search input field is not found or not visible.")

        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        if not search_button:
            self.fail("Search button is not found or not visible.")

        # Check labels for search
        search_label = search_input.get_attribute("placeholder")
        if not search_label or not search_label == "Search store":
            self.fail("Search label is incorrect.")

        # Check for product listing selector
        product_listing = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        if not product_listing:
            self.fail("Product listing is not found or not visible.")

        # Interact with search button
        search_input.send_keys("book")
        search_button.click()

        # Validate search reacted visually (new products should load and be visible)
        products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-item")))
        if not products:
            self.fail("No product items found after search interaction.")

        # Confirm the presence of navigation links like "Home page" in Top menu
        home_page_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
        if not home_page_link:
            self.fail("Home page link is not found or not visible in navigation menu.")

        # Additional checks can be added below following similar patterns

if __name__ == "__main__":
    unittest.main()