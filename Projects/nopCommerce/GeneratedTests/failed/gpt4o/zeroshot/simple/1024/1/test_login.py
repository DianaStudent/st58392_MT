from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to "My account" page
        try:
            my_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {e}")

        # Enter email
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")
        except Exception as e:
            self.fail(f"Failed to find or enter email input: {e}")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to find or enter password input: {e}")

        # Click login
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click login button: {e}")

        # Confirm successful login by checking for "Administration" link presence
        try:
            wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Administration"))
            )
        except Exception as e:
            self.fail("Login failed. 'Administration' link not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()