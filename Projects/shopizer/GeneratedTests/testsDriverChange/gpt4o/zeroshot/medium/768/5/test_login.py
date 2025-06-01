import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click the account icon in the top navigation bar
        account_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pe-7s-user-female")))
        self.assertTrue(account_icon, "Account icon not found.")
        account_icon.click()

        # Click the "Login" link
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link, "Login link not found.")
        login_link.click()

        # Fill in the email field
        email_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.assertTrue(email_field, "Email field not found.")
        email_field.clear()
        email_field.send_keys("test2@user.com")

        # Fill in the password field
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        self.assertTrue(password_field, "Password field not found.")
        password_field.clear()
        password_field.send_keys("test**11")

        # Submit the login form
        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        self.assertTrue(login_button, "Login button not found.")
        login_button.click()

        # Confirm success by checking the URL contains "/my-account"
        self.wait.until(lambda driver: "/my-account" in driver.current_url)
        self.assertIn("/my-account", driver.current_url, "Did not redirect to the My Account page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()