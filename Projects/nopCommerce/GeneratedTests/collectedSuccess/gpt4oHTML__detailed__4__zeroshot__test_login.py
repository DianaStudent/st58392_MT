import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual URL

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "My account" link in the top navigation
        try:
            my_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'My account')))
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find and click My Account link: {str(e)}")

        # Step 3: Wait for the login page to load fully
        try:
            login_title = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Welcome, Please Sign In!"]')))
        except Exception as e:
            self.fail(f"Failed to load login page: {str(e)}")
        
        # Step 4: Fill in the email and password fields
        try:
            email_input = driver.find_element(By.ID, 'Email')
            password_input = driver.find_element(By.ID, 'Password')

            if email_input and password_input:
                email_input.send_keys('admin@admin.com')
                password_input.send_keys('admin')
            else:
                self.fail("Email or Password input field is missing or empty")
        except Exception as e:
            self.fail(f"Failed to locate email or password input fields: {str(e)}")

        # Step 5: Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, 'button.login-button')
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find and click login button: {str(e)}")

        # Step 6: Verify logout button is present, indicating a successful login
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            if not logout_button:
                self.fail("Log out button not found, login may not have been successful")
        except Exception as e:
            self.fail(f"Failed to find log out button: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()