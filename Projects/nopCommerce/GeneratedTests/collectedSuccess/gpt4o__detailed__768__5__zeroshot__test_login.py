from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page.
        driver.get("http://max/")

        # Step 2: Click the "Login" button in the top navigation.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        login_link.click()

        # Step 3: Wait until the login page loads fully.
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        
        self.assertTrue(email_input, "Failed to load login page: Email input field not found")

        # Step 4: Fill in the email and password fields using the provided credentials.
        email_input.send_keys("admin@admin.com")
        password_input = driver.find_element(By.ID, "Password")
        self.assertTrue(password_input, "Password input field not found")
        password_input.send_keys("admin")

        # Step 5: Click the login button.
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        self.assertTrue(login_button, "Login button not found")
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button, "Log out button not found; login might have failed")
        except:
            self.fail("Log out button not found; login might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()