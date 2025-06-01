from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def dynamically_generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@mail.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_btn.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found or clickable: {str(e)}")

        # Click on account button and go to register
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pe-7s-user-female')))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
            register_link.click()
        except Exception as e:
            self.fail(f"Account button/Register link not found or clickable: {str(e)}")

        # Fill the registration form
        email = self.dynamically_generate_email()
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
            email_input.send_keys(email)
            password_input = driver.find_element(By.NAME, 'password')
            password_input.send_keys('test**11')
            repeat_password_input = driver.find_element(By.NAME, 'repeatPassword')
            repeat_password_input.send_keys('test**11')
            first_name_input = driver.find_element(By.NAME, 'firstName')
            first_name_input.send_keys('Test')
            last_name_input = driver.find_element(By.NAME, 'lastName')
            last_name_input.send_keys('User')

            country_dropdown = driver.find_elements(By.TAG_NAME, 'select')[0]
            region_dropdown = driver.find_elements(By.TAG_NAME, 'select')[1]
            country_dropdown.click()
            country_dropdown.send_keys(Keys.DOWN)  # Adjust if more specific needed
            country_dropdown.send_keys(Keys.ENTER)
            region_dropdown.click()
            region_dropdown.send_keys(Keys.DOWN)
            region_dropdown.send_keys(Keys.ENTER)

            register_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            register_submit.click()
        except Exception as e:
            self.fail(f"Error in form filling or submission: {str(e)}")

        # Confirm success by checking URL
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration process did not complete successfully or redirected: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()