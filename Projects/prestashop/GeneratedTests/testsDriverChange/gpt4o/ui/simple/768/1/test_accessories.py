import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            menu = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_top_menu')))
            search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
        except:
            self.fail("Failed to load header elements.")

        # Breadcrumb
        try:
            breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
        except:
            self.fail("Failed to load breadcrumb.")

        # Product list
        try:
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, 'js-product-list')))
        except:
            self.fail("Failed to load product list.")

        # Footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Failed to load footer elements.")
        
        print("All specified UI elements are present and visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()