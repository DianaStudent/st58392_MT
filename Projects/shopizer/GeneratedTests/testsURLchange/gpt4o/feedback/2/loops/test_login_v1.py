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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # Accept cookies
        cookie_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
        )
        cookie_button.click()
        
        # Click on the account icon/button in the top-right
        account_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_icon.click()

        # Wait for the dropdown and click the "Login" link
        login_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Wait for the login form to appear
        username_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")
        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']/..")
        login_button.click()

        # Wait for redirection or page update
        self.wait.until(
            EC.url_contains("/my-account")
        )

        # Confirm successful login by verifying the URL
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login was not successful or wrong redirection.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()