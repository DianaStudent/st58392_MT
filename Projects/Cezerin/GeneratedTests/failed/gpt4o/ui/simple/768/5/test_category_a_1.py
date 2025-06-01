from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSubcategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed())
        except:
            self.fail("Header not found or not visible")

        # Check logo presence
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image img')))
            self.assertTrue(logo.is_displayed())
        except:
            self.fail("Logo not found or not visible")

        # Check search bar presence
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
            self.assertTrue(search_bar.is_displayed())
        except:
            self.fail("Search bar not found or not visible")

        # Check category navigation
        try:
            category_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
            self.assertTrue(category_nav.is_displayed())
        except:
            self.fail("Category navigation not found or not visible")

        # Check breadcrumb navigation
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
            self.assertTrue(breadcrumb.is_displayed())
        except:
            self.fail("Breadcrumb navigation not found or not visible")

        # Check sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
            self.assertTrue(sort_dropdown.is_displayed())
        except:
            self.fail("Sort dropdown not found or not visible")

        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()