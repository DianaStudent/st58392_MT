import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            
            # Check logo
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image img')))
            
            # Check search input
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            
            # Check cart button
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button img')))
        
            # Check breadcrumb
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.breadcrumb')))
            
            # Check category title
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.category-title')))
            
            # Check footer
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        
            # Check footer elements are present
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.footer-contacts')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.footer-menu')))
        
        except Exception as e:
            self.fail(f"UI components are missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()