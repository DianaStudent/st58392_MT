import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        
        # Check header elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        
        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(element.is_displayed(), f"{link_text} link is not visible")
        
        # Check login and register links
        self.check_element_visibility((By.LINK_TEXT, "Login"))
        self.check_element_visibility((By.LINK_TEXT, "Register"))
        
        # Check accept cookies button
        self.check_element_visibility((By.ID, "rcc-confirm-button"))
        
        # Check cart button 
        self.check_element_visibility((By.CLASS_NAME, "icon-cart"))
        
        # Check subscribe form
        self.check_element_visibility((By.NAME, "email"))
        self.check_element_visibility((By.CLASS_NAME, "button"))
        
        # Check footer 
        self.check_element_visibility((By.CLASS_NAME, "footer-area"))

    def check_element_visibility(self, selector):
        try:
            element = self.wait.until(EC.visibility_of_element_located(selector))
            self.assertTrue(element.is_displayed(), f"Element with selector {selector} is not visible")
        except Exception as e:
            self.fail(f"Element with selector {selector} is not found: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()