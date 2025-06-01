import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        # Click the "Account" button in the top right corner.
        account_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='account-button']"))
        )
        account_button.click()

        # Wait for the login page to load.
        login_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-form']"))
        )

        # Enter the email and password using credentials.
        email_field = WebDriverWait(login_form, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-field']"))
        )
        email_field.send_keys("user@test.com")

        password_field = WebDriverWait(login_form, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-field']"))
        )
        password_field.send_keys("testuser")

        # Click the sign-in button.
        sign_in_button = login_form.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
        sign_in_button.click()

        # Verify that the welcome message "Hello user" is present.
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Hello user')]"))
        )
        self.assertTrue(welcome_message.text == "Hello user")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()