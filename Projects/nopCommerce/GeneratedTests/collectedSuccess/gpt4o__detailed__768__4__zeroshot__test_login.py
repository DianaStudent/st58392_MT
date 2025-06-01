import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get("http://max/")

        # Click the "Login" button in the top navigation
        my_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Wait until the login page loads fully
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome, Please Sign In!')]")))

        # Fill in the email and password fields using the provided credentials
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_input = driver.find_element(By.ID, "Password")

        if not email_input or not password_input:
            self.fail("Email or Password input fields are not present or empty.")

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present
        logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))

        if not logout_button:
            self.fail("Log out button is not present, login failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()