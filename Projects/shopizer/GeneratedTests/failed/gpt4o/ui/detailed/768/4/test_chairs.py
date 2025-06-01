from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for header to be visible
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'header-area'))
            )
        except:
            self.fail("Header is not visible")

        # Check for footer
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area'))
            )
        except:
            self.fail("Footer is not visible")

        # Check for navigation links
        nav_links = [
            ('Home', '/'),
            ('Tables', '/category/tables'),
            ('Chairs', '/category/chairs')
        ]
        
        for name, href in nav_links:
            try:
                nav_link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[@href='{href}']"))
                )
            except:
                self.fail(f"Navigation link {name} is not visible")

        # Check for Login and Register buttons
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']"))
            )
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']"))
            )
        except:
            self.fail("Login/Register link is not visible")
        
        # Check and interact with cookie consent button
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'rcc-confirm-button'))
            )
            cookie_button.click()
        except:
            self.fail("Cookie consent button is not visible or not clickable")
        
        # Check the presence and visibility of products
        try:
            product = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'product-wrap'))
            )
        except:
            self.fail("Product section is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()