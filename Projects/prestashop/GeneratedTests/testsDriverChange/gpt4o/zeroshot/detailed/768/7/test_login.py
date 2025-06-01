import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Click the 'Sign in' link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Wait for login form to appear
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        
        # Enter email and password
        email_field.send_keys("test@user.com")
        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        # Click submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Wait for redirect and verify login
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        
        # Check if the sign out button is present
        if not sign_out_link.is_displayed():
            self.fail("Sign out button not displayed, login might have failed.")

        # Check if the username is displayed
        try:
            user_name = driver.find_element(By.XPATH, "//span[contains(text(), 'test user')]")
            self.assertTrue(user_name.is_displayed())
        except:
            self.fail("Username 'test user' not found, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()