from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        
        # Open homepage and click login link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.user-info a[href*="login"]'))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Sign in link not found: {str(e)}")

        # Wait for login page to load and fill in login form
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'field-email'))
            )
            password_input = driver.find_element(By.ID, 'field-password')
            submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')

            email_input.send_keys("test@user.com")
            password_input.send_keys("test@user1")
            submit_button.click()

        except Exception as e:
            self.fail(f"Login form elements not found or interaction failed: {str(e)}")

        # Wait for redirect and check login success
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a.logout'))
            )
            username_display = driver.find_element(By.CSS_SELECTOR, 'a.account span.hidden-sm-down')

            self.assertIn("Sign out", sign_out_link.text)
            self.assertTrue(username_display.text)

        except Exception as e:
            self.fail(f"Login confirmation elements not found or incorrect: {str(e)}")


if __name__ == "__main__":
    unittest.main()