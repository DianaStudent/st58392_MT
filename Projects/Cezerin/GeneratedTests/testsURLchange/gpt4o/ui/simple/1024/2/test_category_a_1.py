import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.driver.maximize_window()
        
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check for header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            
            # Check for main logo
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
            
            # Check for search box
            search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box')))
            search_input = search_box.find_element(By.CLASS_NAME, 'search-input')
            
            # Check for main navigation links
            nav_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
            
            # Check for product category title
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
            
            # Check for breadcrumb navigation
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
            
            # Check for footer
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            
            # Verify footer contains company links
            company_links = footer.find_element(By.CLASS_NAME, 'footer-menu')
            
        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()