from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_shop_react_app(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root')))
        
        # Verify navigation links
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, '.nav-links')
        self.assertGreater(len(nav_links), 0)
        
        # Verify form fields (login and register)
        login_form = self.driver.find_element(By.CSS_SELECTOR, '#login-form')
        register_form = self.driver.find_element(By.CSS_SELECTOR, '#register-form')
        self.assertIsNotNone(login_form)
        self.assertIsNotNone(register_form)

        # Interact with one or two elements
        chairs_link = self.driver.find_element(By.LINK_TEXT, 'Chairs')
        chairs_link.click()
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.chairs-container')))
        
        # Verify that interactive elements do not cause errors in the UI
        details_button = self.driver.find_element(By.CSS_SELECTOR, '#details-button')
        details_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()