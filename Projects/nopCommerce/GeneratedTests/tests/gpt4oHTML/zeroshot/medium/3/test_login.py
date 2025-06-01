import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()  # Handle zoom manually if needed
        self.base_url = "http://yourwebsite.com"  # Adjust to the correct base URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get(self.base_url)
        
        # Click the "Login" link
        try:
            login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            self.assertTrue(login_link.is_displayed(), "Login link is not displayed.")
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find and click 'My account' link: {str(e)}")

        # Step 3: Wait for the login page to load
        try:
            page_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome, Please Sign In!')]")))
            self.assertTrue(page_title.is_displayed(), "Login page did not load properly.")
        except Exception as e:
            self.fail(f"Login page did not load properly: {str(e)}")

        # Step 4: Enter the email and password
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_input = driver.find_element(By.ID, "Password")
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to enter login credentials: {str(e)}")

        # Step 5: Click the login button to submit the form
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            self.assertTrue(login_button.is_displayed(), "Login button is not displayed.")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click login button: {str(e)}")

        # Step 6: Verify that the user is logged in by checking "Log out" button
        try:
            logout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button.is_displayed(), "Log out button is not displayed. User may not be logged in.")
        except Exception as e:
            self.fail(f"Log out button is not present, user might not be logged in: {str(e)}")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()