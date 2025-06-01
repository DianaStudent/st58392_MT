import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")  # Use an appropriate base URL

    def tearDown(self):
        # Tear down the driver
        self.driver.quit()

    def test_login_process(self):
        driver = self.driver

        # Step 1: Open the home page (already done in setUp)
        
        # Step 2: Click the "Login" button in the top navigation
        try:
            customer_info_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            customer_info_link.click()
        except:
            self.fail("My account link was not found")

        # Step 3: Wait until the login page loads fully
        try:
            # Wait for the login form to be present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
        except:
            self.fail("Login page did not load fully")

        # Step 4: Fill in the email and password fields using the provided credentials
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = driver.find_element(By.ID, "Password")
            
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except:
            self.fail("Email or Password input fields not found")

        # Step 5: Click the login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-1.login-button"))
            )
            login_button.click()
        except:
            self.fail("Login button not found or not clickable")

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("User is not logged in: Log out button not found")

if __name__ == "__main__":
    unittest.main()