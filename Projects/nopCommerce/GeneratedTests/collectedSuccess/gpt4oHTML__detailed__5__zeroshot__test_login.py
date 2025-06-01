import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page
        driver.get("http://max/")  # Replace with the actual URL

        # Step 2: Click the "Login" button in the top navigation
        try:
            my_account_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile a[href='/customer/info']"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find 'My account' link: {str(e)}")
        
        # Step 3: Wait until the login page loads fully
        try:
            login_title = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title h1"))
            )
            assert login_title.is_displayed()
        except Exception as e:
            self.fail(f"Login page failed to load properly: {str(e)}")

        # Step 4: Fill in the email and password fields using the provided credentials
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to input credentials: {str(e)}")
        
        # Step 5: Click the login button
        try:
            login_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-1.login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click on the login button: {str(e)}")

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation
        try:
            logout_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".admin-header-links a[href='/Admin']"))
            )
            assert logout_link.is_displayed()
        except Exception as e:
            self.fail(f"Logout link is not present after login: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()