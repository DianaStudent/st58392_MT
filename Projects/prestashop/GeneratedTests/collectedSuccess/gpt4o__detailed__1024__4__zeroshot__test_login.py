from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click the login link from the top navigation.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Wait for the login page to load.
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields using test credentials provided.
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.clear()
        email_input.send_keys("test@user.com")

        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.clear()
        password_input.send_keys("test@user1")

        # Step 5: Click the submit button.
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login.
        wait.until(EC.presence_of_element_located((By.ID, "header")))

        # Step 7: Confirm that login was successful.
        sign_out = driver.find_elements(By.LINK_TEXT, "Sign out")
        user_info = driver.find_elements(By.XPATH, "//span[contains(text(),'test user')]")

        if not sign_out or not user_info:
            self.fail("Login was not successful. 'Sign out' button or username not found.")

        # Additional check for visibility
        self.assertTrue(sign_out[0].is_displayed(), "'Sign out' button is not visible")
        self.assertTrue(user_info[0].is_displayed(), "Username is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()