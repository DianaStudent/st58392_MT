import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertIsNotNone(header)
            
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertIsNotNone(register_link)
            
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.assertIsNotNone(login_link)

            cart_link = self.wait.until(EC.visibility_of_element_located((By.ID, "topcartlink")))
            self.assertIsNotNone(cart_link)
        
        except Exception as e:
            self.fail(f"Header elements verification failed: {str(e)}")
        
        # Verify search box
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            self.assertIsNotNone(search_box)
            
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertIsNotNone(search_input)
            
            search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            self.assertIsNotNone(search_button)
        
        except Exception as e:
            self.fail(f"Search box verification failed: {str(e)}")
        
        # Verify menu links
        try:
            top_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertIsNotNone(top_menu)
            
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            self.assertIsNotNone(home_link)
            
            new_products_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            self.assertIsNotNone(new_products_link)
        
        except Exception as e:
            self.fail(f"Menu links verification failed: {str(e)}")
    
        # Verify slider
        try:
            slider = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nop-slider")))
            self.assertIsNotNone(slider)
        
        except Exception as e:
            self.fail(f"Slider verification failed: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()