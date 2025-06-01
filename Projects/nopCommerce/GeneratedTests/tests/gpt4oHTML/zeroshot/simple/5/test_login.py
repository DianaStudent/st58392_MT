import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://example.com")  # Replace with the actual URL

    def test_login_process(self):
        driver = self.driver

        # Wait for the login button and click it
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find 'My account' link: {str(e)}")

        # Find email and password fields and fill them
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            password_field = driver.find_element(By.ID, "Password")

            email_field.send_keys("admin@admin.com")
            password_field.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to find email or password fields: {str(e)}")

        # Click the login button
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find the login button: {str(e)}")

        # Confirm successful login by checking the presence of the "Administration" link
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except Exception as e:
            self.fail(f"Login failed, 'Administration' link not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()