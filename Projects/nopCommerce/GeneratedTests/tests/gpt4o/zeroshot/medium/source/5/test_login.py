import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver

        # Verify "Log in" link exists and click it
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            self.assertIsNotNone(login_link, "Log in link is not found.")
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click login link: {str(e)}")

        # Wait and verify login page load
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            self.assertIsNotNone(email_field, "Email input field is not found on login page.")
        except Exception as e:
            self.fail(f"Failed to load login page or find email input field: {str(e)}")

        # Enter email and password
        try:
            email_field.clear()
            email_field.send_keys("admin@admin.com")
            password_field = driver.find_element(By.ID, "Password")
            password_field.clear()
            password_field.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to enter login credentials: {str(e)}")

        # Click login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            self.assertIsNotNone(login_button, "Login button is not found.")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click login button: {str(e)}")

        # Verify successful login
        try:
            logout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertIsNotNone(logout_button, "Log out button is not found, login might have failed.")
        except Exception as e:
            self.fail(f"Verification of login failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()