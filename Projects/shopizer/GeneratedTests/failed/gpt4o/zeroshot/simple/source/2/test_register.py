from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()
        except:
            self.fail("Accept cookies button not found.")

        # Navigate to Register page
        try:
            account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            ActionChains(driver).move_to_element(account_btn).perform()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found.")

        # Fill registration form
        email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
        
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email_input.send_keys(email)
            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")
            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")
            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")
            country_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(1)")
            country_select.click()
            driver.find_element(By.XPATH, "//option[text()='Canada']").click()
            state_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(2)")
            state_select.click()
            driver.find_element(By.XPATH, "//option[text()='Quebec']").click()
        except:
            self.fail("Registration form fields not found.")

        # Submit form
        try:
            register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_button.click()
        except:
            self.fail("Register button not found.")

        # Verify successful registration
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Did not redirect to /my-account page after registration.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()