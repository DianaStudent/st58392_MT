from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome Driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        # Open the page
        self.driver.get("http://example.com/category-a-1")  # Update URL as necessary

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirm presence of navigation links
        header_selector = By.TAG_NAME, "header"
        home_link_selector = By.XPATH, "//a[@href='/' and @class='logo-image active']"
        category_a_link_selector = By.XPATH, "//a[@href='/category-a']"
        subcategory_1_link_selector = By.XPATH, "//a[@href='/category-a-1' and @class='is-active']"

        # Check header existence
        header = wait.until(EC.visibility_of_element_located(header_selector), "Header is not visible.")
        if header is None:
            self.fail("Header is missing")

        # Check navigation links existence
        home_link = wait.until(EC.visibility_of_element_located(home_link_selector), "Home link is not visible.")
        category_a_link = wait.until(EC.visibility_of_element_located(category_a_link_selector), "Category A link is not visible.")
        subcategory_1_link = wait.until(EC.visibility_of_element_located(subcategory_1_link_selector), "Subcategory 1 link is not visible.")
        
        if not home_link or not category_a_link or not subcategory_1_link:
            self.fail("One or more key navigation links are missing.")

        # Interact with an element - search input and check visual update
        search_input_selector = By.CLASS_NAME, 'search-input'
        search_icon_selector = By.CLASS_NAME, 'search-icon-search'

        search_input = wait.until(EC.visibility_of_element_located(search_input_selector), "Search input is not visible.")
        search_icon = wait.until(EC.visibility_of_element_located(search_icon_selector), "Search icon is not visible.")

        if not search_input or not search_icon:
            self.fail("Search elements are missing.")

        search_input.send_keys("test")
        search_icon.click()

        # Confirm that search input text is retained (UI update check)
        updated_search_input = wait.until(
            EC.text_to_be_present_in_element_value(search_input_selector, "test"),
            "Search input did not update.")

        if not updated_search_input:
            self.fail("Search input did not update correctly after interaction.")

    def tearDown(self):
        # Close browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()