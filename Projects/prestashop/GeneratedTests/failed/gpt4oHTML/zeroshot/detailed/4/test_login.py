from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        
        # Step 1: Open the homepage is already done in setUp
        
        # Step 2: Click the login link from the top navigation.
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        login_link.click()

        # Step 3: Wait for the login page to load.
        self.wait.until(
            EC.presence_of_element_located((By.ID, "login-form"))
        )

        # Step 4: Fill in the email and password fields.
        email_input = driver.find_element(By.ID, "field-email")
        password_input = driver.find_element(By.ID, "field-password")
        
        if not email_input or not password_input:
            self.fail("Email or password input field is not present or empty.")
        
        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")
        
        # Step 5: Click the submit button.
        submit_button = driver.find_element(By.ID, "submit-login")
        
        if not submit_button:
            self.fail("Submit button is not present or empty.")
        
        submit_button.click()

        # Step 6: Wait for the redirect after login.
        self.wait.until(
            EC.presence_of_element_located((By.ID, "index"))
        )

        # Step 7: Confirm that login was successful.
        signout_link = driver.find_elements(By.LINK_TEXT, "Sign out")
        username_element = driver.find_elements(By.XPATH, "//span[contains(text(), 'test user')]")

        if not signout_link:
            self.fail("Sign out link not found in top navigation.")

        if not username_element:
            self.fail("Username not visible in top navigation.")

        # Assertions
        self.assertTrue(len(signout_link) > 0, "Sign out button is not present.")
        self.assertTrue(len(username_element) > 0, "Username is not visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()