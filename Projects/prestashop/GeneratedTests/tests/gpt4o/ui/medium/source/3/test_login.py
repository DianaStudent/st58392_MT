import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Confirm navigation links presence
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertIsNotNone(home_link, "Home link is not visible")

            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertIsNotNone(clothes_link, "Clothes link is not visible")

            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.assertIsNotNone(accessories_link, "Accessories link is not visible")

            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            self.assertIsNotNone(art_link, "Art link is not visible")

            # Confirm input fields are present
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_input, "Email input is not visible")

            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_input, "Password input is not visible")

            # Confirm buttons are present
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button, "Sign in button is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(register_link, "Register link is not visible")

            # Interact with sign in button and ensure no UI errors
            sign_in_button.click()
            # Verify a UI element that indicates page change (e.g., error message, content change) is visible
            error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "help-block")))
            self.assertIsNotNone(error_message, "Error message after clicking sign in is not visible")
        
        except Exception as e:
            self.fail(f"UI test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()