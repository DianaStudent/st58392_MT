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
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_structure(self):
        driver = self.driver
        
        # Check that header is visible
        self.assert_element_visible(By.CLASS_NAME, 'header-area')
        
        # Check that footer is visible
        self.assert_element_visible(By.CLASS_NAME, 'footer-area')
        
        # Check that navigation links are visible
        nav_links = ['/', '/category/tables', '/category/chairs', '/login', '/register']
        for link in nav_links:
            self.assert_element_visible(By.XPATH, f"//a[@href='{link}']")
        
        # Check presence and visibility of main content sections
        self.assert_element_visible(By.CLASS_NAME, 'site-blocks-cover')
        self.assert_element_visible(By.CLASS_NAME, 'support-area')
        self.assert_element_visible(By.CLASS_NAME, 'product-area')
        self.assert_element_visible(By.CLASS_NAME, 'subscribe-area-3')
        
        # Interact with UI elements
        self.interact_with_element(By.ID, 'rcc-confirm-button')  # Accept cookies button
        
        # Check buttons in product action
        self.assert_element_visible(By.CLASS_NAME, 'fa-shopping-cart')
        self.assert_element_visible(By.CLASS_NAME, 'fa-eye')
        
        # Check subscription form visibility
        self.assert_element_visible(By.NAME, 'email')
        self.assert_element_visible(By.CLASS_NAME, 'button')
        
        # Confirm that key UI sections react visually
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'react-toast-notifications__container')))
        
        # Assert that no required elements are missing
        self.check_missing_elements()
    
    def assert_element_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
        except:
            self.fail(f'Element with {by}="{value}" is missing or not visible.')
        self.assertTrue(element.is_displayed(), f'Element with {by}="{value}" should be visible.')
    
    def interact_with_element(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            element.click()
        except:
            self.fail(f'Could not interact with element with {by}="{value}".')
    
    def check_missing_elements(self):
        # List of required UI elements (for example)
        required_elements = [
            (By.CLASS_NAME, 'header-area'),
            (By.CLASS_NAME, 'footer-area'),
            (By.NAME, 'email'),
            (By.CLASS_NAME, 'button'),
            (By.XPATH, "//a[@href='/login']")
        ]
        
        for by, value in required_elements:
            try:
                self.wait.until(EC.visibility_of_element_located((by, value)))
            except:
                self.fail(f'Required UI element with {by}="{value}" is missing or not visible.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()