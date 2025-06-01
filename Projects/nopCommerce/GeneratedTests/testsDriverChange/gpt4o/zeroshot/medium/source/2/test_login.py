import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Open the home page and click the "My account" link
        try:
            my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            self.assertTrue(my_account_link.is_displayed(), "My account link is not displayed")
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find My account link: {str(e)}")

        # Wait for the login page to load
        try:
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not displayed")
        except Exception as e:
            self.fail(f"Failed to load the login page: {str(e)}")

        # Enter the email and password
        email_input.send_keys("admin@admin.com")
        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("admin")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
            self.assertTrue(login_button.is_displayed(), "Login button is not displayed")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find Login button: {str(e)}")

        # Verify login by checking "Log out" button presence
        try:
            logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_link.is_displayed(), "Log out link is not displayed")
        except Exception as e:
            self.fail(f"Failed to log in or verify login: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()