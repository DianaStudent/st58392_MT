import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Step 1: Open the home page
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.user-info a[href*="login"]'))
            )
        except Exception as e:
            self.fail(f"Home page did not load correctly: {str(e)}")

        # Step 2: Click on the login link in the top menu
        login_link = driver.find_element(By.CSS_SELECTOR, '.user-info a[href*="login"]')
        login_link.click()

        # Step 3: Wait for the login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'form#login-form'))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {str(e)}")

        # Step 4: Fill in the email and password fields
        email_input = driver.find_element(By.CSS_SELECTOR, '#field-email')
        password_input = driver.find_element(By.CSS_SELECTOR, '#field-password')

        # Ensure the input fields are present and not empty
        if not email_input or not password_input:
            self.fail("Email or Password input field is missing or not found")

        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Step 5: Submit the login form
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button#submit-login')
        if not submit_button:
            self.fail("Submit button is missing or not found")
        submit_button.click()

        # Step 6: Verify that login was successful by checking for "Sign out"
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.user-info a.logout'))
            )
            sign_out_text = driver.find_element(By.CSS_SELECTOR, '.user-info a.logout').text
            self.assertEqual(sign_out_text, "Sign out", "Login was not successful, 'Sign out' not found")
        except Exception as e:
            self.fail(f"Login verification failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()