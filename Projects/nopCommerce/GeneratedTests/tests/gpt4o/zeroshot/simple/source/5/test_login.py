import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver

        try:
            # Navigate to the login page
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()

            # Enter email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")

            # Enter password
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")

            # Click Log in
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            login_button.click()

            # Confirm success by checking the "Administration" link is present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "administration"))
            )

        except TimeoutException:
            self.fail("Element not found or page took too long to load.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()