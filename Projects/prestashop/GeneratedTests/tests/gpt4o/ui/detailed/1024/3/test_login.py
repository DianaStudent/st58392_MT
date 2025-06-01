import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify main navigation is present and visible
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Verify login form elements
        login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        self.assertTrue(login_form.is_displayed(), "Login form is not visible")

        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertTrue(email_input.is_displayed(), "Email input is not visible")

        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")

        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertTrue(sign_in_button.is_displayed(), "Sign-in button is not visible")

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Interact with the Sign-in button
        sign_in_button.click()

        # Add further interactions and checks as needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()