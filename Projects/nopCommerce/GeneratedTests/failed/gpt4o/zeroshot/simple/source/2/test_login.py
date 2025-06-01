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

    def test_login(self):
        driver = self.driver

        # Navigate to login page
        try:
            my_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            my_account_link.click()
        except Exception:
            self.fail("My account link is not available")

        try:
            # Enter email
            email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Email")))
            email_input.send_keys("admin@admin.com")
            
            # Enter password
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")
            
            # Click login button
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()

            # Confirm success by checking "Log out" presence
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out")))
        except Exception:
            self.fail("Login process failed or 'Log out' button is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()