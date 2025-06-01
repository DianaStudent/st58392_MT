from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_page_elements(self):
        driver = self.driver
        driver.get("http://localhost:3000/category-a-1")

        try:
            # Wait and verify header navigation links
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a'))
            )
            self.assertTrue(len(nav_links) > 0, "Navigation links are missing")

            # Verify search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input'))
            )
            self.assertIsNotNone(search_input, "Search input is missing or not visible")

            # Verify category title
            category_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.category-title'))
            )
            self.assertEqual(category_title.text, "Subcategory 1", "Category title is incorrect or missing")

            # Verify footer links
            footer_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.footer-menu a'))
            )
            self.assertTrue(len(footer_links) > 0, "Footer links are missing")

            # Interact with an element - click on search icon
            search_icon = driver.find_element(By.CSS_SELECTOR, 'img.search-icon-search')
            search_icon.click()

            # Confirm no errors appear in the UI (as observed)
            # Assuming there is no visible error element after interactions
            WebDriverWait(driver, 20).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-message'))
            )

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()