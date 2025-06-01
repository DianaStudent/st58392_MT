from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure you have chromedriver in PATH
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        # Wait for and click "My account" link to go to login page
        my_account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Wait for and enter email
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        email_field.send_keys("admin@admin.com")

        # Wait for and enter password
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        password_field.send_keys("admin")

        # Wait for and click login button
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button"))
        )
        login_button.click()

        # Confirm success by checking the presence of "Log out" button
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Log out link not found, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()