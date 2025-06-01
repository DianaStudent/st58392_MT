import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def generate_random_email(self):
        # Generate a random email address
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        driver.get('http://localhost/')  # Change URL as necessary
        wait.until(EC.presence_of_element_located((By.ID, 'root')))

        # 2. Click on the account button and select "Register".
        account_setting_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active')))
        account_setting_button.click()

        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Register')))
        if not register_link:
            self.fail("Register link not found")
        register_link.click()

        # 3. Fill in the registration form.
        form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-register-form')))
        if not form:
            self.fail("Register form not found")

        email_input = form.find_element(By.NAME, 'email')
        password_input = form.find_element(By.NAME, 'password')
        repeat_password_input = form.find_element(By.NAME, 'repeatPassword')
        first_name_input = form.find_element(By.NAME, 'firstName')
        last_name_input = form.find_element(By.NAME, 'lastName')

        test_email = self.generate_random_email()
        email_input.send_keys(test_email)
        password_input.send_keys('test**11')
        repeat_password_input.send_keys('test**11')
        first_name_input.send_keys('Test')
        last_name_input.send_keys('User')

        # 4. Select a country and a region/state.
        country_select = form.find_elements(By.TAG_NAME, 'select')[0]
        country_select.click()
        country_option = country_select.find_element(By.XPATH, "//option[@value='CA']")
        if not country_option:
            self.fail("Country option not found")
        country_option.click()

        state_select = form.find_elements(By.TAG_NAME, 'select')[1]
        state_select.click()
        state_option = state_select.find_element(By.XPATH, "//option[@value='QC']")
        if not state_option:
            self.fail("State option not found")
        state_option.click()

        # 5. Submit the registration form.
        register_button = form.find_element(By.XPATH, "//button[@type='submit']")
        register_button.click()

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url, "URL did not contain '/my-account'")

    def tearDown(self):
        # Clean up and close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()