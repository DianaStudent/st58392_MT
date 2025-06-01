import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_login_process(self):
        driver = self.driver

        # Click on 'Sign in' link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Sign in']]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail("Sign in link not found: " + str(e))

        # Wait for and fill the login form
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            password_input = driver.find_element(By.ID, "field-password")

            email_input.send_keys("test@user.com")
            password_input.send_keys("test@user1")
        except Exception as e:
            self.fail("Login form elements not found: " + str(e))

        # Submit the login form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except Exception as e:
            self.fail("Could not click submit button: " + str(e))

        # Verify login success by checking "Sign out" link presence
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[span[text()='Sign out']]"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link not found, login might have failed.")
        except Exception as e:
            self.fail("Failed to verify login success: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()