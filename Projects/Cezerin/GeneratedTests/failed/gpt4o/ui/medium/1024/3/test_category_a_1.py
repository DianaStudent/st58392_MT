from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header and navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category B')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category C')))
        except:
            self.fail("Header or navigation links are missing")

        # Check search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input is missing")

        # Check sorting dropdown
        try:
            sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select')))
        except:
            self.fail("Sort dropdown is missing")

        # Verify the presence of a button (Filter products)
        try:
            filter_button = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(), 'Filter products')]")))
        except:
            self.fail("Filter button is missing")
        
        # Verify breadcrumb navigation
        try:
            breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
        except:
            self.fail("Breadcrumb is missing")

        # Interact with an element: enter text in search input
        search_input.send_keys("query")
        # Ensure the text value is entered as expected
        self.assertEqual(search_input.get_attribute('value'), 'query')

        # Verify footer presence
        try:
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()