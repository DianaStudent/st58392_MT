from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        wait = self.wait

        try:
            # Wait for the account icon/button to be present and click it
            account_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'account-setting-active')))
            account_icon.click()

            # Wait for the dropdown and click the "Login" link
            login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
            login_link.click()

            # Wait for the login form to appear
            username_field = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
            password_field = wait.until(EC.element_to_be_clickable((By.NAME, 'loginPassword')))
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Login"]')))

            # Fill in the username and password fields using credentials
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")

            # Click the login button
            login_button.click()

            # Wait for redirection or page update
            wait.until(EC.url_contains("/my-account"))

            # Confirm successful login by checking the URL
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)

        except Exception as e:
            self.fail(f"Test failed due to {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()