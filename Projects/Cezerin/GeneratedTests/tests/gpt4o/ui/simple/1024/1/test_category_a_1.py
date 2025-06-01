import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements_presence(self):
        try:
            # Check header presence
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header, "Header is missing")

            # Check logo presence
            logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='logo-image active']/img")))
            self.assertIsNotNone(logo, "Logo is missing")

            # Check search box presence
            search_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box")))
            self.assertIsNotNone(search_box, "Search box is missing")

            # Check category title
            category_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
            self.assertIsNotNone(category_title, "Category title is missing")

            # Check sort dropdown
            sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select")))
            self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing")

            # Check footer presence
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer, "Footer is missing")
        
        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()