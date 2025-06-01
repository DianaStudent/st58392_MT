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
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
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
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Sign out')]"))
            )

            # Check if "Sign out" is present after login
            sign_out_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign out')]")
            self.assertTrue(sign_out_element.is_displayed(), "Sign out link is not displayed after login")

        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()