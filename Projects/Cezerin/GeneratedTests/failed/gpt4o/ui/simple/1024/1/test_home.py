from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_elements(self):
        try:
            # Check for header
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check for logo
            logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check for search input
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check for primary navigation
            primary_nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
            self.assertTrue(primary_nav.is_displayed(), "Primary navigation is not visible")

            # Check for category links
            category_a_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            self.assertTrue(category_a_link.is_displayed(), "Category A link is not visible")

            category_b_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category B')))
            self.assertTrue(category_b_link.is_displayed(), "Category B link is not visible")

            category_c_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category C')))
            self.assertTrue(category_c_link.is_displayed(), "Category C link is not visible")

            # Check for Best Sellers section
            best_sellers_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))
            self.assertTrue(best_sellers_title.is_displayed(), "Best Sellers title is not visible")

            # Check for footer
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()