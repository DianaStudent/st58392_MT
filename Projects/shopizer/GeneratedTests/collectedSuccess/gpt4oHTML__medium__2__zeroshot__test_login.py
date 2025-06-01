import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Use the correct URL for your homepage
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver

        # Step 1: Open the homepage.
        driver.get("http://localhost/")  # Use the correct URL for your homepage

        # Step 2: Click the account icon in the top navigation bar.
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon not found or clickable: {e}")

        # Step 3: Click the "Login" link.
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or clickable: {e}")

        # Step 4: Fill in the email and password fields.
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self.assertNotEqual(email_input.get_attribute("placeholder"), "")
            email_input.send_keys("test2@user.com")

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            self.assertNotEqual(password_input.get_attribute("placeholder"), "")
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Error interacting with login form fields: {e}")

        # Step 5: Submit the login form.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-box button[type='submit']"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or clickable: {e}")

        # Step 6: Confirm success by checking the URL.
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"The page did not redirect to '/my-account': {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()