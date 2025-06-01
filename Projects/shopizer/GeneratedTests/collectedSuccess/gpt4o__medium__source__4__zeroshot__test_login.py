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
        self.driver.maximize_window()
        self.base_url = "http://localhost/"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # WebDriverWait initialization
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies if the button is available
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies.click()
        except:
            pass  # If no cookies button, continue

        # Click on the account icon
        account_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.account-setting-active')))
        account_icon.click()

        # Click the "Login" link
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()
        
        # Wait for the login form to appear and fill it in
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, 'loginPassword')))
        
        if not username_input or not password_input:
            self.fail("Login form fields are missing.")
        
        username_input.clear()
        username_input.send_keys("test2@user.com")
        
        password_input.clear()
        password_input.send_keys("test**11")

        # Submit the login form
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()

        # Verify successful login by checking redirection to "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Login failed or did not redirect to /my-account.")

if __name__ == "__main__":
    unittest.main()