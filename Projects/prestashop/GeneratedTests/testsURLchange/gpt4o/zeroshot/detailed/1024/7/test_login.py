from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields using test credentials provided
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logout")))

        # Step 7: Confirm that login was successful
        sign_out_button = driver.find_elements(By.LINK_TEXT, "Sign out")
        user_info = driver.find_elements(By.XPATH, "//*[contains(text(), 'test user')]")

        if not sign_out_button or not user_info:
            self.fail("Sign out button or username not present after login. Login failed.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()