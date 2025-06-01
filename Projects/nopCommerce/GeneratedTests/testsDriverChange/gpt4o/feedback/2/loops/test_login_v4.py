import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Open the home page and click the "My account" link in the top navigation
        try:
            login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link. Exception: {str(e)}")

        # Wait for the login page to load
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        except Exception as e:
            self.fail(f"Email field not found on login page. Exception: {str(e)}")

        # Fill in the email and password fields with provided credentials
        try:
            email_field.send_keys("admin@admin.com")
            password_field = driver.find_element(By.ID, "Password")
            password_field.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to fill in credentials. Exception: {str(e)}")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click login button. Exception: {str(e)}")

        # Verify the user is logged in by checking for the "Log out" button
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button.is_displayed(), "Log out button should be visible after logging in.")
        except Exception as e:
            self.fail(f"Log out button not found or not visible after login, login process failed. Exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()