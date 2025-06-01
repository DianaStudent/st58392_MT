import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver

        # Verify structural elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(header.is_displayed())
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Header or Footer is missing.")

        # Verify presence and visibility of input fields, buttons, labels
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
            remember_me_checkbox = driver.find_element(By.ID, "RememberMe")
            forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot password?")
            
            self.assertTrue(email_input.is_displayed())
            self.assertTrue(password_input.is_displayed())
            self.assertTrue(login_button.is_displayed())
            self.assertTrue(register_button.is_displayed())
            self.assertTrue(remember_me_checkbox.is_displayed())
            self.assertTrue(forgot_password_link.is_displayed())
        except:
            self.fail("A key UI element is missing.")

        # Interact with key UI elements
        login_button.click()

        # Confirm UI reacts visually
        try:
            error_message = self.wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
            self.assertTrue(error_message.is_displayed())
        except:
            self.fail("No error message displayed after attempting login with empty fields.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()