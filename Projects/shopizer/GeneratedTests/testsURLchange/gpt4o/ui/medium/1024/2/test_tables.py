import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopUIElementsTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Verify navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            tables_link = driver.find_element(By.LINK_TEXT, 'Tables')
            chairs_link = driver.find_element(By.LINK_TEXT, 'Chairs')
        except:
            self.fail("Navigation links are missing")

        # Verify presence of header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))
        except:
            self.fail("Header logo is missing")
        
        # Verify the presence of buttons
        try:
            accept_cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Accept cookie button is missing")
        
        # Interact with elements
        try:
            accept_cookie_button.click()
            navbar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except Exception as e:
            self.fail(f"Error interacting with UI elements: {str(e)}")

        # Verify the presence of footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
            contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
        except:
            self.fail("Footer elements are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()