from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # Accept cookies if the button is present
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass  # If no cookie button, proceed

        # Click on the account icon/button in the top-right
        account_icon = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_icon.click()

        # Wait for the dropdown and click the "Login" link
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Wait for the login form to appear
        username_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )

        # Fill in the username and password fields using credentials
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = driver.find_element(By.XPATH, '//button/span[text()="Login"]/..')
        login_button.click()

        # Wait for redirection or page update and confirm successful login
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.myaccount-area"))
        )
        current_url = driver.current_url
        if "/my-account" not in current_url:
            self.fail("Login failed, '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()