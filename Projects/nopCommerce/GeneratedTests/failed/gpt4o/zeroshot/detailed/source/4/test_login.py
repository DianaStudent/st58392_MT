from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        homepage_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/customer/info']"))
        )
        if not homepage_link or not homepage_link.text.strip():
            self.fail("Failed to find the 'My account' link")

        homepage_link.click()

        # Step 2: Click the "Login" button in the top navigation
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.register-button"))
        )
        if not login_button or not login_button.text.strip():
            self.fail("Failed to find the 'Register' button")

        login_button.click()

        # Step 3: Wait until the login page loads
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        if not email_input:
            self.fail("Email input not found")

        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        if not password_input:
            self.fail("Password input not found")
        
        # Step 4: Fill in the email and password fields
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Step 5: Click the login button
        login_submit = driver.find_element(By.CSS_SELECTOR, "button.login-button")
        if not login_submit or not login_submit.text.strip():
            self.fail("Login button not found")

        login_submit.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present
        logout_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        if not logout_link or not logout_link.text.strip():
            self.fail("Log out button not found, login might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()