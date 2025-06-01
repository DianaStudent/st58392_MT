from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage (already done in setUp)

        # 2. Click the login link from the top navigation
        sign_in_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='_desktop_user_info']//a[span[contains(text(), 'Sign in')]]")))
        sign_in_link.click()
        
        # 3. Wait for the login page to load
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Log in to your account')]")))
        
        # 4. Fill in the email and password fields using test credentials provided
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "field-email")))
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "field-password")))

        email_field.clear()
        email_field.send_keys("test@user.com")

        password_field.clear()
        password_field.send_keys("test@user1")
        
        # 5. Click the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        submit_button.click()

        # 6. Wait for the redirect after login
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@class, 'logout') and text()='Sign out']")))

        # 7. Confirm that login was successful
        #    - The "Sign out" button is present in the top navigation
        sign_out_button = driver.find_elements(
            By.XPATH, "//a[contains(@class, 'logout') and text()='Sign out']")
        
        if not sign_out_button:
            self.fail("Sign out button not found or not visible.")

        #    - The username (e.g. "test user") is also visible in the top navigation.
        username_element = driver.find_elements(
            By.XPATH, "//a[contains(@class, 'account')]/span[contains(text(), 'test user')]")
        
        if not username_element:
            self.fail("Username 'test user' not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()