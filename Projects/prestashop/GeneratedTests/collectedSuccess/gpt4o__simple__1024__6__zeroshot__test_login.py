import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver

        # Wait for the "Sign in" link and click it
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()

        # Wait for the email input field
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        email_input.send_keys("test@user.com")

        # Wait for the password input field
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        password_input.send_keys("test@user1")

        # Wait for the "Sign in" button
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "submit-login"))
        )
        sign_in_button.click()

        # Check if "Sign out" is present after login
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except:
            self.fail("Sign out link not found, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()