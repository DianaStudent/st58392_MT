from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login_successfully(self):
        # Click the login link from the top navigation
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='login']")))
        login_link.click()

        # Fill in the email and password fields using test credentials provided
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        email_field.send_keys("test@user.com")

        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_field.send_keys("test@user1")

        # Click the submit button
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='submit']")))
        submit_button.click()

        # Wait for the redirect after login
        WebDriverWait(self.driver, 20).until(EC.url_to_be("http://localhost:8080/en/"))

        # Confirm that login was successful by checking that:
        # - The "Sign out" button is present in the top navigation
        sign_out_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='sign-out']")))

        # - The username (e.g. "test user") is also visible in the top navigation.
        username_label = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@data-name='username']")))
        self.assertEqual(username_label.text, "test user")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()