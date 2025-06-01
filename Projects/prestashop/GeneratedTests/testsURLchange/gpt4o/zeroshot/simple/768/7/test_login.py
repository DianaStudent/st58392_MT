from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Click 'Sign in' link
            sign_in_link = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()

            # Fill in email
            email_input = wait.until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys("test@user.com")

            # Fill in password
            password_input = driver.find_element(By.ID, "field-password")
            password_input.send_keys("test@user1")

            # Click 'Sign in' button
            sign_in_button = driver.find_element(By.ID, "submit-login")
            sign_in_button.click()

            # Confirm login success by checking 'Sign out' link
            sign_out_link = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link)

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()