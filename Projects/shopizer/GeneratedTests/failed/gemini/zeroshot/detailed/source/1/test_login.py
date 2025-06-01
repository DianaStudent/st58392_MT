from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.email = "test2@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Click on the account icon
        account_icon = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_icon.click()

        # Click the "Login" link
        login_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()

        # Wait for the login form to appear
        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Fill in the username and password fields
        username_field.send_keys(self.email)
        password_field = driver.find_element(By.NAME, "loginPassword")
        password_field.send_keys(self.password)

        # Click the login button
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()

        # Wait for redirection or page update and check the URL
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

if __name__ == "__main__":
    unittest.main()