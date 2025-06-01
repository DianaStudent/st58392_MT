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

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Find and click the "My account" link to go to the login page
        try:
            my_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find My account link: {str(e)}")

        # Enter email
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            email_input.send_keys("admin@admin.com")
        except Exception as e:
            self.fail(f"Failed to find Email input: {str(e)}")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to find Password input: {str(e)}")

        # Click login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find Login button: {str(e)}")

        # Confirm login by checking if "Log out" button is present
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
        except Exception as e:
            self.fail(f"Login was not successful: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()