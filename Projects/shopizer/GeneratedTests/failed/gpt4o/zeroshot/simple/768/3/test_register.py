from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()

            # Navigate to Register page
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()

            # Fill out registration form
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email_input.send_keys("test_user_{0}@example.com".format(int(time.time())))
            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")
            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")
            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")
            country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
            country_select.send_keys("Canada")
            state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
            state_select.send_keys("Quebec")

            # Submit form
            register_button = driver.find_element(By.XPATH, "//button[span[text()='Register']]")
            register_button.click()

            # Check for successful registration
            wait.until(EC.url_contains("/my-account"))
        
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()