import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        # Click on the "My account" to go to the login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'My account'))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {str(e)}")

        # Enter email and password
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'Email'))
            )
            password_field = driver.find_element(By.ID, 'Password')
        except Exception as e:
            self.fail(f"Email or Password field is missing: {str(e)}")

        email_field.send_keys('admin@admin.com')
        password_field.send_keys('admin')

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, 'button.login-button')
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click login button: {str(e)}")

        # Verify that the "Log out" button is present
        try:
            log_out_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Log out'))
            )
            assert log_out_button.is_displayed(), "'Log out' button is not displayed"
        except Exception as e:
            self.fail(f"Login failed or 'Log out' button is not present: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)