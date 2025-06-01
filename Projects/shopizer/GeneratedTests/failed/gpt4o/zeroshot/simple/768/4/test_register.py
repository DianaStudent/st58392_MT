from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Accept cookies button not found.")

        # Go to Register page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found.")

        # Fill in registration form
        email = f"test_{self.generate_random_string(6)}@example.com"
        password = "test**11"

        try:
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")
            country_select = driver.find_element(By.XPATH, "//select[option='Select a country']")
            state_select = driver.find_element(By.XPATH, "//select[option='Select a state']")

            email_input.send_keys(email)
            password_input.send_keys(password)
            repeat_password_input.send_keys(password)
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            country_select.send_keys("Canada")
            state_select.send_keys("Quebec")

            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
            register_button.click()
        except:
            self.fail("Failed to fill the registration form.")

        # Confirm registration success
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Registration was not successful, '/my-account' not in URL.")

    def tearDown(self):
        self.driver.quit()

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    unittest.main()