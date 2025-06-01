from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or any other WebDriver you prefer
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        
        # Navigate to login page
        try:
            my_account = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account.click()
        except TimeoutException:
            self.fail("Failed to find My account link")

        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")
        except TimeoutException:
            self.fail("Email input field not found")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")
        except TimeoutException:
            self.fail("Password input field not found")

        # Click login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()
        except TimeoutException:
            self.fail("Login button not found")

        # Confirm success by checking for the "Log out" button
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
        except TimeoutException:
            self.fail("Log out button not found, login might have failed")


if __name__ == "__main__":
    unittest.main()