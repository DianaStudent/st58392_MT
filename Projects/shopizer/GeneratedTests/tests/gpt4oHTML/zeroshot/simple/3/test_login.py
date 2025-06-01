import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver (use the appropriate driver for your browser)
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080")  # Include your base URL

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies if present
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            print("Cookies consent not found or unable to click")

        # Click on the account icon to open the account dropdown
        try:
            account_icon_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon_button.click()
        except Exception as e:
            self.fail(f"Account icon not found or clickable: {str(e)}")

        # Click on the Login link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or clickable: {str(e)}")

        # Wait for the login form to be visible and fill in credentials
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            email_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Login form fields not found or interactable: {str(e)}")

        # Submit the login form
        try:
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or clickable: {str(e)}")
        
        # Check if redirected to the user's account page
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Redirection to the account page failed: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()