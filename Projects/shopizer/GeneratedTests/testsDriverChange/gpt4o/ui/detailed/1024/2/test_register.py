import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertIsNotNone(header, "Header is not visible.")

        # Verify footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Verify navigation menu items
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(link, f"Navigation link {link_text} is not visible.")
        
        # Verify login/register form elements
        login_form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-register-form')))
        self.assertIsNotNone(login_form, "Login/Register form is not visible.")

        # Check presence of form fields
        form_fields = [
            ('email', 'Email address'),
            ('password', 'Password'),
            ('repeatPassword', 'Repeat Password'),
            ('firstName', 'First Name'),
            ('lastName', 'Last Name'),
            ('stateProvince', 'State')
        ]
        
        for field_name, placeholder in form_fields:
            field = wait.until(EC.visibility_of_element_located((By.NAME, field_name)))
            self.assertIsNotNone(field, f"Form field {field_name} with placeholder {placeholder} is not visible.")
        
        # Check button presence and clickability
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']"))
        )
        self.assertIsNotNone(submit_button, "Register button is not visible or clickable.")
        submit_button.click()
        
        # Verify UI reacts visually, e.g., by checking some post-click state
        # Check some UI response here, if any
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()