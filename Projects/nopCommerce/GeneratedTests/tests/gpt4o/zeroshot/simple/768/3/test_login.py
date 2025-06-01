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
        wait = self.wait

        # Navigate to login page
        my_account_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Enter email
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        email_field.send_keys("admin@admin.com")

        # Enter password
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        password_field.send_keys("admin")

        # Click login button
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        login_button.click()

        # Verify successful login by checking for "Log out" button
        try:
            log_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Log out button not found. Login failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()