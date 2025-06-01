import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Uncomment to run tests headlessly
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/")  # URL needs to be the base URL of the application
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 1: Click the account icon in the top navigation bar
        try:
            account_icon = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".same-style.account-setting"))
            )
        except:
            self.fail("Account icon is not present or couldn't be located")
        
        account_icon.click()

        # Step 2: Click the "Login" link
        try:
            login_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
        except:
            self.fail("Login link is not present or couldn't be located")

        login_link.click()

        # Step 3: Fill in the email and password fields
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        except:
            self.fail("Email input field is not present or couldn't be located")

        email_input.clear()
        email_input.send_keys("test2@user.com")

        try:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Password input field is not present or couldn't be located")

        password_input.clear()
        password_input.send_keys("test**11")

        # Step 4: Submit the login form
        try:
            submit_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']/span[text()='Login']"))
            )
        except:
            self.fail("Login submit button is not present or couldn't be located")
        
        submit_button.click()

        # Step 5: Confirm success by checking if URL contains "/my-account"
        try:
            self.wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Browser did not navigate to the '/my-account' URL, indicating login was not successful")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()