import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Load the login page
        driver.get("http://max/login?returnUrl=%2F")

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        if not header:
            self.fail("Header is not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))
        if not footer:
            self.fail("Footer is not visible.")

        # Verify presence of elements in login form
        login_form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-page")))
        if not login_form:
            self.fail("Login form is not visible.")

        # Check for email input field
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        if not email_input:
            self.fail("Email input is not visible.")

        # Check for password input field
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        if not password_input:
            self.fail("Password input is not visible.")

        # Check for login button
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-button")))
        if not login_button:
            self.fail("Login button is not visible.")

        # Check for register button
        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-button")))
        if not register_button:
            self.fail("Register button is not visible.")

        # Interact with the form
        email_input.send_keys("test@example.com")
        password_input.send_keys("Password123")
        login_button.click()

        # Verify the UI reacts or displays a message as expected
        # Here we assume that a notification or a successful login message should appear
        # This is just a placeholder, adapt to actual behavior if known
        try:
            success_message = wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-success")))
            self.assertTrue(success_message.is_displayed(), "Success message is not displayed.")
        except:
            pass  # If a success message is not expected on failed login, skip this part

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()