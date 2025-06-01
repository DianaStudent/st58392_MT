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

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check for footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer.is_displayed():
            self.fail("Footer is not visible")
        
        # Check for navigation elements
        navigation_links = driver.find_elements(By.CSS_SELECTOR, '.nav-level-0 a')
        if len(navigation_links) < 1:
            self.fail("Navigation links are missing")

        # Check for search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        if not search_input.is_displayed():
            self.fail("Search input is not visible")

        # Check presence of breadcrumb
        breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
        if not breadcrumb.is_displayed():
            self.fail("Breadcrumb is not visible")
        
        # Check presence of sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        if not sort_dropdown.is_displayed():
            self.fail("Sort dropdown is not visible")

        # Interact with breadcrumb to ensure UI reacts
        home_breadcrumb = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home')))
        home_breadcrumb.click()

        # Verify if redirected to home page
        home_page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'title')))
        if "Home" not in driver.title:
            self.fail("Failed to navigate to home page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()