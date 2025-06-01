import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # Find 'My account' link and click it
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        # Find email input field and enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.clear()
            email_input.send_keys("admin@admin.com")
        except Exception as e:
            self.fail(f"Could not find or interact with email input: {e}")

        # Find password input field and enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.clear()
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Could not find or interact with password input: {e}")

        # Find login button and click it
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click login button: {e}")

        # Verify successful login by checking for the presence of 'Administration' link
        try:
            administration_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
            self.assertTrue(administration_link.is_displayed(), "Administration link is not displayed after login.")
        except Exception as e:
            self.fail(f"Could not find Administration link after login: {e}")

if __name__ == "__main__":
    unittest.main()