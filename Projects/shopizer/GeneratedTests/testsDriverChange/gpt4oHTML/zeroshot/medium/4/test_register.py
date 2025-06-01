import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterTest(unittest.TestCase):
    def setUp(self):
        # Set up the driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        # Dynamically generate an email
        return f"test_{"".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))}@user.com"

    def test_register(self):
        driver = self.driver
        wait = self.wait
        email = self.generate_email()

        # Step 1: Open the home page
        driver.get("http://localhost/")  # Replace with the correct URL

        # Accept cookies if the button is available
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass  # If no cookie button or already accepted

        # Step 2: Click on the account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 3 and Step 4: Fill in the registration form with all fields and select country/state
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_input.send_keys(email)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("test**11")

        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_input.send_keys("test**11")

        first_name_input = driver.find_element(By.NAME, "firstName")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys("User")

        country_select = driver.find_element(By.XPATH, '//select[option[text()="Select a country"]]')
        country_select.click()
        country_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[text()="Canada"]')))
        country_option.click()

        state_select = driver.find_element(By.XPATH, '//select[option[text()="Select a state"]]')
        state_select.click()
        state_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[text()="Quebec"]')))
        state_option.click()

        # Step 5: Submit the registration form
        submit_button = driver.find_element(By.XPATH, '//button/span[text()="Register"]')
        submit_button.click()

        # Step 6: Wait for redirect and confirm success
        time.sleep(2)  # Short pause for redirect
        current_url = driver.current_url

        self.assertIn("/my-account", current_url, "The page was not redirected to the my-account page.")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()