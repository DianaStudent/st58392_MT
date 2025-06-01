import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        email = self.generate_random_email()
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        # Accept cookies if present
        try:
            accept_cookies_btn = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()
        except:
            pass

        # Click on the account icon/button
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # Select the "Register" option
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        repeat_password_input = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))

        email_input.send_keys(email)
        password_input.send_keys(password)
        repeat_password_input.send_keys(password)
        first_name_input.send_keys(firstname)
        last_name_input.send_keys(lastname)

        # Select country and state
        country_select = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a country']]"))))
        country_select.select_by_index(1)

        # Ensure state selector is loaded
        state_select = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a state']]"))))
        state_select.select_by_index(1)

        # Submit the form
        register_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[span[text()='Register']]")))
        register_button.click()

        # Confirm registration success
        success_url_condition = EC.url_contains("/my-account")
        if not wait.until(success_url_condition):
            self.fail("Registration did not succeed, URL does not contain '/my-account'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()