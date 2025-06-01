from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com/category-a-1")  # Change to the actual test URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header element is missing")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer element is missing")

        # Check navigation and its links
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.nav-level-0 a')))
        self.assertTrue(len(nav_links) > 0, "Navigation links are missing")

        # Check the sort input field
        sort_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        self.assertIsNotNone(sort_select, "Sort select input is missing")

        # Check the search box input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertIsNotNone(search_input, "Search input is missing")

        # Check and interact with search button
        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        self.assertIsNotNone(search_button, "Search button is missing")
        search_button.click()

        # Interaction with subcategory links and assert visibility
        subcategory_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.nav-level-1 a')))
        self.assertTrue(len(subcategory_links) > 0, "Subcategory links are missing")

        # Click on "Subcategory 1" link if it exists
        subcategory_1 = driver.find_element(By.CSS_SELECTOR, 'a[href="/category-a-1"]')
        self.assertIsNotNone(subcategory_1, "Subcategory 1 link is missing")
        subcategory_1.click()

        # Assert that body tag is visible after clicking
        body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
        self.assertIsNotNone(body, "Body element is missing after navigation")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()