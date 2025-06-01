import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        ).click()

    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to the registration form
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
        )
        account_button.click()

        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # Fill in the registration form
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        random_email = f"testuser_{random.randint(1000,9999)}@example.com"
        email_input.send_keys(random_email)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("test**11")

        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_input.send_keys("test**11")

        first_name_input = driver.find_element(By.NAME, "firstName")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys("User")

        country_select = driver.find_element(By.XPATH, "//select[option='Select a country']")
        country_select.send_keys(Keys.DOWN)  # Select "Canada"
        
        state_select = driver.find_element(By.XPATH, "//select[option='Select a state']")
        state_select.send_keys(Keys.DOWN)  # Select first state

        # Submit the registration form
        register_button = driver.find_element(By.XPATH, "//button[span='Register']")
        register_button.click()

        # Verify successful registration by checking if redirected to the "/my-account" page
        WebDriverWait(driver, 20).until(
            EC.url_contains("/my-account")
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()