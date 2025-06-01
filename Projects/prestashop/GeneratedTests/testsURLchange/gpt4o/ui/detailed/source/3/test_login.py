import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is missing or not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is missing or not visible")

        # Check navigation
        try:
            navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation is missing or not visible")

        # Check email input
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email input is missing or not visible")

        # Check password input
        try:
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password input is missing or not visible")

        # Check sign in button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Sign in button is missing or not visible")

        # Check forgot password link
        try:
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("Forgot password link is missing or not visible")

        # Check 'No account? Create one here' link
        try:
            no_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("No account link is missing or not visible")

        # Interact with the password visibility toggle
        try:
            show_password_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-action='show-password']")))
            show_password_button.click()
        except:
            self.fail("Password show/hide toggle is not functioning or missing")

        # Check reaction: Password input should change type from 'password' to 'text' or vice versa
        try:
            current_type = wait.until(lambda drv: drv.find_element(By.ID, "field-password").get_attribute("type"))
            self.assertIn(current_type, ["password", "text"], "Password type toggle failed")
        except:
            self.fail("Password visibility toggle did not work as expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()