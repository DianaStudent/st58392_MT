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


class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click on the account icon/button
        account_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # Step 2: Select the "Register" option
        register_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/register']")))
        register_button.click()

        # Step 3: Wait for the registration page to load
        wait.until(EC.presence_of_element_located(
            (By.NAME, "email")))

        # Generating dynamic email
        random_suffix = random.randint(100000, 999999)
        email = f"test_{random_suffix}@user.com"

        # Step 4: Fill in registration details
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(email)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("test**11")

        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_input.send_keys("test**11")

        first_name_input = driver.find_element(By.NAME, "firstName")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys("User")

        # Step 5: Select the first country
        country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
        country_select.click()
        country = driver.find_element(By.XPATH, "//select/option[@value='CA']")
        country.click()

        # Pause to ensure state selection can be made
        time.sleep(1)

        # Step 6: Select the state
        state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
        state_select.click()
        state = driver.find_element(By.XPATH, "//select/option[@value='QC']")
        state.click()

        # Step 7: Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[span[text()='Register']]")
        submit_button.click()

        # Step 8: Wait for redirect to "/my-account"
        wait.until(EC.url_contains("/my-account"))
        if "/my-account" not in driver.current_url:
            self.fail("Registration failed, did not redirect to 'my-account'.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()