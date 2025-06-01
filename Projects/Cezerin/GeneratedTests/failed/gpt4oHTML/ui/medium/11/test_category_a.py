from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://yourwebsite.com/category-a")  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        
        # Check for header presence
        try:
            header = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except:
            self.fail("Header not found")

        # Check for navigation links presence
        try:
            nav_links = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .cat-parent a"))
            )
            self.assertGreater(len(nav_links), 0, "Navigation links not found or not visible")
        except:
            self.fail("Navigation links not found")

        # Check for the search input presence
        try:
            search_input = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-box .search-input"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except:
            self.fail("Search input not found or not visible")

        # Check for button presence (Filter products in mobile view or close button)
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, ".button.is-fullwidth")
            self.assertTrue(filter_button.is_displayed(), "Filter button is not visible")
        except:
            self.fail("Filter button not found or not visible")

    def test_ui_interaction(self):
        driver = self.driver
        
        # Interact with the search input
        try:
            search_input = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-box .search-input"))
            )
            search_input.send_keys("Product A" + Keys.ENTER)
            
            # Verify if input interaction caused any UI change like highlighting or suggestion dropdown
            search_icon = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-icon-search"))
            )
            self.assertTrue(search_icon.is_displayed(), "Search icon is not visible after interaction")
        except:
            self.fail("Search interaction failed or did not update the UI")

        # Check if clicking the category link works and updates the UI
        try:
            category_link = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary-nav .cat-parent a[href='/category-a']"))
            )
            category_link.click()
            
            # Check if the title or breadcrumb changed to confirm navigation
            category_title = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".category-title"))
            )
            self.assertEqual(category_title.text, "Category A", "Category page did not load properly after clicking")
        except:
            self.fail("Failed to navigate to Category A or UI did not update")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()