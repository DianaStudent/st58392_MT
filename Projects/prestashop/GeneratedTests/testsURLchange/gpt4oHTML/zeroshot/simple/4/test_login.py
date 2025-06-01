import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
        self.driver.get("http://localhost:8080/en/")  # Replace with the actual URL if different

    def test_login(self):
        driver = self.driver

        try:
            # Wait for the "Sign in" link and click it
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except TimeoutException:
            self.fail("Sign in link not found or not clickable")

        try:
            # Wait for the email field and enter the email
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys("test@user.com")
        except TimeoutException:
            self.fail("Email field not found or not interactable")

        try:
            # Wait for the password field and enter the password
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys("test@user1")
        except TimeoutException:
            self.fail("Password field not found or not interactable")

        try:
            # Wait for the submit button and click it
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            submit_button.click()
        except TimeoutException:
            self.fail("Submit button not found or not clickable")

        try:
            # Confirm success by checking for "Sign out" text
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link not displayed after login")
        except TimeoutException:
            self.fail("Sign out link not found after login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()