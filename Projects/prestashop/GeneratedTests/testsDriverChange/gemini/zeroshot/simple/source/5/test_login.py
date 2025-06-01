import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        try:
            # Find the "Sign in" link and click it
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Sign in']]"))
            )
            sign_in_link.click()

            # Find the email input field and enter the email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys("test@user.com")

            # Find the password input field and enter the password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys("test@user1")

            # Find the submit button and click it
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            submit_button.click()

            # Wait for the "Sign out" link to appear, indicating successful login
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[.//span[text()='Sign out']]"))
            )

            # Check that "Sign out" is present
            sign_out_element = driver.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
            self.assertIn("Sign out", sign_out_element.text)

        except Exception as e:
            self.fail(f"Login failed: {e}")

if __name__ == "__main__":
    unittest.main()