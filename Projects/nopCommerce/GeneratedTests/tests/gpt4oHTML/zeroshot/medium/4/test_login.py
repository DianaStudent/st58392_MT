import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver

        # Step 1: Open the home page.
        driver.get("http://yourwebsite.com")  # Replace with the actual URL

        # Step 2: Click the "Login" link.
        try:
            my_account_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            self.assertTrue(my_account_link.is_displayed(), "My account link is not displayed.")
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {str(e)}")

        # Step 3: Wait for the login page to load.
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome, Please Sign In!')]")))
        except Exception as e:
            self.fail(f"Login page did not load properly: {str(e)}")

        # Step 4: Enter the email and password.
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.NAME, "Email")))
            password_field = driver.find_element(By.NAME, "Password")
            self.assertTrue(email_field.is_displayed(), "Email field is not displayed.")
            self.assertTrue(password_field.is_displayed(), "Password field is not displayed.")
            email_field.send_keys("admin@admin.com")
            password_field.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to enter email or password: {str(e)}")

        # Step 5: Click the login button to submit the form.
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            self.assertTrue(login_button.is_displayed(), "Login button is not displayed.")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click the login button: {str(e)}")

        # Step 6: Verify that the user is logged in by checking the "Log out" button.
        try:
            logout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button.is_displayed(), "Log out button is not displayed.")
        except Exception as e:
            self.fail("Log out button was not found after login, user might not be logged in.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()