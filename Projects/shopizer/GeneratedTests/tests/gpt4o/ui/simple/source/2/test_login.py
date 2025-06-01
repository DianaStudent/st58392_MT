import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header and main menu items
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertIsNotNone(header, "Header area is missing.")

        menu_items_text = ["Home", "Tables", "Chairs"]
        for text in menu_items_text:
            menu_item = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
            self.assertIsNotNone(menu_item, f"Menu item '{text}' is missing.")

        # Verify login button
        login_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertIsNotNone(login_button, "Login button is missing.")

        # Verify register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_button, "Register button is missing.")

        # Verify the email and password fields on the login form
        login_email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        self.assertIsNotNone(login_email_field, "Email address input is missing.")

        login_password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        self.assertIsNotNone(login_password_field, "Password input is missing.")

        # Verify the login form submit button
        login_form_submit_button = self.wait.until(EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit' and span[text()='Login']]")))
        self.assertIsNotNone(login_form_submit_button, "Login form submit button is missing.")

        # Verify the cookie consent button
        cookie_consent_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(cookie_consent_button, "Cookie consent button is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()