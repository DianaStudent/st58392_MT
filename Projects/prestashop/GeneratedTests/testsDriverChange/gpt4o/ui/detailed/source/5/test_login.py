import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")
        
        # Check if navigation links are visible
        for link_id in ["label-log-in", "label-register"]:
            link = wait.until(EC.visibility_of_element_located((By.ID, link_id)))
            if not link.is_displayed():
                self.fail(f"Navigation link {link_id} is not visible")

        # Check email input field
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        if not email_field.is_displayed():
            self.fail("Email input field is not visible")

        # Check password input field
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        if not password_field.is_displayed():
            self.fail("Password input field is not visible")

        # Check sign in button
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        if not sign_in_button.is_displayed():
            self.fail("Sign in button is not visible")

        # Interact with the sign in button
        sign_in_button.click()

        # Check forgot password link
        forgot_password = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        if not forgot_password.is_displayed():
            self.fail("Forgot password link is not visible")

        # Check create account link
        create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        if not create_account_link.is_displayed():
            self.fail("Create account link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()