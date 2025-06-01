import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        try:
            driver = self.driver
            wait = self.wait
            
            # Accept cookies if the button is present
            try:
                accept_cookies_button = wait.until(
                    EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
                )
                accept_cookies_button.click()
            except:
                print("Accept cookies button not present")

            # Click the account icon
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female"))
            )
            account_icon.click()

            # Click the Login link
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Wait for the login form
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )

            # Fill in the email and password fields
            email_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")

            # Submit the login form
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Login']/.."))
            )
            login_button.click()

            # Confirm success by checking URL
            success_url_part = "/my-account"
            self.assertTrue(
                wait.until(EC.url_contains(success_url_part)),
                "Login failed or redirection not to /my-account"
            )

        except Exception as e:
            self.fail(f"Test failed due to {str(e)}")

    def tearDown(self):
        # Tear down WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()