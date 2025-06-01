import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        
        # Wait for and click on "My account"
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Wait for email input to ensure login page has loaded
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )

        # Fill in email and password
        email_input.send_keys("admin@admin.com")

        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
        login_button.click()

        # Verify the "Log out" link is present
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertIsNotNone(logout_link)
        except Exception as e:
            self.fail("Log out link not found. Login failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()