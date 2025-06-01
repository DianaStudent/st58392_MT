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

        # Click on "My account" to go to the login page
        my_account_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Wait for login form to be visible
        wait.until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )

        # Enter email
        email_input = driver.find_element(By.ID, "Email")
        email_input.clear()
        email_input.send_keys("admin@admin.com")

        # Enter password
        password_input = driver.find_element(By.ID, "Password")
        password_input.clear()
        password_input.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        login_button.click()

        # Confirm success by checking the presence of "Log out" in the top navigation
        try:
            wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Login failed or 'Log out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()