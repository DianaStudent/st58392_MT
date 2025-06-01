from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace Chrome with your preferred browser driver
        self.driver.get("http://localhost:8000")  # Replace with actual URL

    def test_login(self):
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-name='email']"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-name='password']"))
        )
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Clicking the submit button might be necessary
        login_button.click()

        # Wait until the sign out text appears
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span[data-name='sign-out']"), "Sign out")
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()