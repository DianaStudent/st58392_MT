import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Step 1: Assert Home page loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Log in'))
            )
        except Exception as e:
            self.fail("Home page did not load properly: " + str(e))

        # Step 2: Click the "Login" link.
        login_link = driver.find_element(By.LINK_TEXT, 'Log in')
        login_link.click()

        # Step 3: Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//h1[text()="Welcome, Please Sign In!"]'))
            )
        except Exception as e:
            self.fail("Login page did not load properly: " + str(e))

        # Step 4: Enter the email and password.
        email_input = driver.find_element(By.ID, 'Email')
        password_input = driver.find_element(By.ID, 'Password')
        
        if not email_input or not password_input:
            self.fail("Email or Password input field not found")

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Step 5: Click the login button to submit the form.
        login_button = driver.find_element(By.CSS_SELECTOR, 'button.button-1.login-button')
        
        if not login_button:
            self.fail("Login button not found")
        
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present.
        try:
            logout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Log out'))
            )
            self.assertTrue(logout_button.is_displayed())
        except Exception as e:
            self.fail("Log out button not found after login: " + str(e))

if __name__ == '__main__':
    unittest.main()