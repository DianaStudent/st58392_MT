import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click the login link from the top navigation.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Wait for the login page to load.
        login_header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(login_header.text.strip(), "Log in to your account", "Login page did not load correctly.")
        
        # Step 4: Fill in the email and password fields using test credentials provided.
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed.")
        email_input.send_keys("test@user.com")
        
        self.assertTrue(password_input.is_displayed(), "Password input is not displayed.")
        password_input.send_keys("test@user1")

        # Step 5: Click the submit button.
        submit_button = driver.find_element(By.ID, "submit-login")
        self.assertTrue(submit_button.is_displayed(), "Submit button is not displayed.")
        submit_button.click()

        # Step 6: Wait for the redirect after login.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-info")))

        # Step 7: Confirm that login was successful.
        try:
            sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            account_name = driver.find_element(By.XPATH, '//a[@class="account"]//span[@class="hidden-sm-down"]')
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed after login.")
            self.assertTrue(account_name.is_displayed(), "Account name is not displayed after login.")
            self.assertEqual(account_name.text.strip(), "test user", "Logged in user name is not correct.")
        except Exception as e:
            self.fail(f"Login verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()