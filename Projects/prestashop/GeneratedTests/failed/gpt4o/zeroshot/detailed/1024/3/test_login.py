from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get(self.base_url)

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields using test credentials provided
        email_input = driver.find_element(By.ID, "field-email")
        password_input = driver.find_element(By.ID, "field-password")
        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.ID, "index")))

        # Step 7: Confirm that login was successful
        try:
            sign_out_link = driver.find_element(By.LINK_TEXT, "Sign out")
            user_info = driver.find_element(By.CSS_SELECTOR, ".user-info .account span.hidden-sm-down")

            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")
            self.assertTrue(user_info.is_displayed(), "User info is not displayed")
            self.assertEqual(user_info.text, "test user", "Username does not match")
        except Exception as e:
            self.fail(f"Login confirmation failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()