from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver

        # Step 1: Wait for and click the 'Sign in' link in the top menu
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a/span[text()='Sign in']"))
            )
        except:
            self.fail("Sign in link not found or not loaded.")
        
        sign_in_link.click()

        # Step 2: Wait for the login page to load by checking for the presence of the login form
        try:
            login_form = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "login-form"))
            )
        except:
            self.fail("Login form not found or not loaded.")

        # Step 3: Fill in the email and password fields
        email_field = login_form.find_element(By.ID, "field-email")
        password_field = login_form.find_element(By.ID, "field-password")

        if not email_field or not password_field:
            self.fail("Email or Password field not found or empty.")

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 4: Submit the login form
        submit_button = login_form.find_element(By.ID, "submit-login")

        if not submit_button:
            self.fail("Submit button not found or not loaded.")

        submit_button.click()

        # Step 5: Verify that login was successful by checking for the presence of "Sign out" in the top bar
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='logout hidden-sm-down' and span[text()='Sign out']]"))
            )
        except:
            self.fail("Sign out link not found or not loaded.")

        self.assertTrue(sign_out_link.is_displayed(), "Log in failed, 'Sign out' link not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()