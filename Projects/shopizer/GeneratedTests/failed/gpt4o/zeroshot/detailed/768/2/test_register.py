from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{random_string}@user.com"

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the home page and accept cookies if present
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass

        # 2. Click on the account icon/button
        account_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting button")))
        account_icon.click()

        # 3. Select the "Register" option
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # 4. Wait for the registration page to load
        registration_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-rb-event-key='register']")))

        # 5. Fill in all fields
        email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        first_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))

        email = self.generate_email()
        email_input.send_keys(email)
        password_input.send_keys("test**11")
        repeat_password_input.send_keys("test**11")
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")

        # 6. Select a first country from the dropdown
        country_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[option[text()='Select a country']]")))
        country_select.click()
        country_select.find_element(By.XPATH, ".//option[text()='Canada']").click()

        # 7. Select a first state only after selecting country
        state_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[option[text()='Select a state']]")))
        state_select.click()
        state_select.find_element(By.XPATH, ".//option[text()='Quebec']").click()

        # Click outside to make sure dropdowns hide
        driver.find_element(By.TAG_NAME, "body").click()

        # 8. Submit the form
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]")))
        submit_button.click()

        # 9. Wait for the page to redirect and confirm registration success
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url, "Registration failed: '/my-account' not in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()