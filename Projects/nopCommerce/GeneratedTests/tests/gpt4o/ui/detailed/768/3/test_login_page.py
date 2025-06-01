import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visible(self):
        driver = self.driver

        # Check visibility of header, footer and main sections
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            main_section = self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
        except:
            self.fail("Main structural elements are not visible")

        # Check presence of login fields
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button")))
        except:
            self.fail("Login input fields or buttons are missing")

        # Verify clickable elements
        try:
            register_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.register-button")))
            forgot_password_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot password?")))
        except:
            self.fail("Interactive elements like buttons or links are not clickable")

        # Interact and verify elements' reactions
        try:
            email_field.send_keys("test@example.com")
            password_field.send_keys("password")
            login_button.click()
            # Verify impact on UI after interaction
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification-container")))
        except:
            self.fail("Interaction with UI elements did not yield expected results")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()