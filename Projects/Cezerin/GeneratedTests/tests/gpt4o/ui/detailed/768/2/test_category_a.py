import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_UI_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible.")
        
        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is not visible.")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        except:
            self.fail("Category title is not visible.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except:
            self.fail("Search input is not visible.")

        # Check main menu links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".nav-level-0 .cat-parent a")))
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are visible.")
        except:
            self.fail("Navigation links are not visible.")

        # Check product items
        try:
            product_items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "available")))
            self.assertGreaterEqual(len(product_items), 2, "Not all product items are visible.")
        except:
            self.fail("Product items are not visible.")

        # Check sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select select")))
        except:
            self.fail("Sort dropdown is not visible.")

        # Interact with sort dropdown
        try:
            sort_dropdown.click()
            sort_option = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select select option[value='-date_created']")))
            sort_option.click()
        except:
            self.fail("Failed to interact with sort dropdown.")
        
        # Confirm that interaction took place (This is just a placeholder for actual visual confirmation)
        # For a real interaction test, more UI changes must be checked.

if __name__ == "__main__":
    unittest.main()