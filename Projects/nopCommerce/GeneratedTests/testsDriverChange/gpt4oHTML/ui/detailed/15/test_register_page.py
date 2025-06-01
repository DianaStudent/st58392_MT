import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.driver.get(self.base_url + "register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Check the presence of the header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        except:
            self.fail("Header not found or not visible.")
        
        # Check presence of the footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))
        except:
            self.fail("Footer not found or not visible.")
        
        # Check the presence of the top navigation menu
        try:
            top_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".top-menu.notmobile")))
        except:
            self.fail("Top navigation menu not found or not visible.")
        
        # Check the presence of the registration form
        try:
            reg_form = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".registration-page form")))
        except:
            self.fail("Registration form not found or not visible.")
        
        # Check fields and button within the registration form
        required_elements = {
            "gender_male": "input#gender-male",
            "gender_female": "input#gender-female",
            "first_name": "input#FirstName",
            "last_name": "input#LastName",
            "email": "input#Email",
            "password": "input#Password",
            "confirm_password": "input#ConfirmPassword",
            "register_button": "button#register-button"
        }
        
        for element_name, selector in required_elements.items():
            try:
                elm = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            except:
                self.fail(f"The required element '{element_name}' with selector '{selector}' was not found or not visible.")

        # Interact with UI elements
        try:
            self.driver.find_element(By.CSS_SELECTOR, "input#first_name").send_keys("John")
            self.driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys("Doe")
            self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("johndoe@example.com")
            self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Password123")
            self.driver.find_element(By.CSS_SELECTOR, "input#confirm_password").send_keys("Password123")
            self.driver.find_element(By.CSS_SELECTOR, "button#register-button").click()
        except Exception as e:
            self.fail(f"Interaction with UI elements failed: {str(e)}")
        
        # Check that the UI reacts visually (e.g., loading spinner or redirect)
        try:
            # Assuming a page transition or notification would appear
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#dialog-notifications-success")))
        except:
            self.fail("Visual confirmation after form submission failed or not found.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()