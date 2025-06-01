import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get('http://max/')
        
        # Step 2: Click the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'My account')))
        if not login_link:
            self.fail("Login link not found on the home page.")
        login_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, 'Email')))

        # Step 4: Enter the email and password
        email_input = driver.find_element(By.ID, 'Email')
        password_input = driver.find_element(By.ID, 'Password')
        if not email_input or not password_input:
            self.fail("Email or Password input field not found on the login page.")

        email_input.send_keys('admin@admin.com')
        password_input.send_keys('admin')

        # Step 5: Click the login button to submit the form
        login_button = driver.find_element(By.CLASS_NAME, 'login-button')
        if not login_button:
            self.fail("Login button not found on the login page.")
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Log out')))
            if not logout_button.is_displayed():
                self.fail("Log out button is not displayed; login might have failed.")
        except:
            self.fail("Log out button not found in top navigation; login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()