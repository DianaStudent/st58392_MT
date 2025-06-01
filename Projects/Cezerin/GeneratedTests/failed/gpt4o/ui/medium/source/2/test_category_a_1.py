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
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:3000"

    def test_ui_elements(self):
        driver = self.driver
        driver.get(f"{self.base_url}/category-a-1")
        
        # Check if the header is present and visible
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
        except:
            self.fail("Header is not present or visible.")
        
        # Check if the category 'Subcategory 1' is present
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1"))
            )
        except:
            self.fail("Subcategory 1 link is not present or visible.")

        # Check if the search input is present and visible
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input"))
            )
        except:
            self.fail("Search input is not present or visible.")

        # Check if the sort dropdown is present and interact
        try:
            sort_dropdown = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select"))
            )
            sort_dropdown.click()
        except:
            self.fail("Sort dropdown is not present, interactable, or visible.")
        
        # Check if the footer is present and visible
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "footer"))
            )
        except:
            self.fail("Footer is not present or visible.")
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()