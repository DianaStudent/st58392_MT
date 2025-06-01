from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the consent button is present
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except Exception:
            pass

        # Click on the account icon/button
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Select "Register" option
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Generate a dynamic email address
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"test_{random_str}@user.com"

        # Fill in the registration form fields
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")
        
        # Select the first country from the dropdown
        country_dropdown = driver.find_element(By.XPATH, "//select[option='Select a country']")
        country_dropdown.click()
        country_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[2]")))
        country_option.click()
        
        # Wait for the state dropdown to load and select first state
        state_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[option='Select a state']")))
        state_dropdown.click()
        state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[2]")))
        state_option.click()

        # Submit the registration form
        register_button = driver.find_element(By.XPATH, "//button[@type='submit'][span='Register']")
        register_button.click()

        # Confirm registration success by checking the URL
        wait.until(EC.url_contains("/my-account"))
        if "/my-account" not in driver.current_url:
            self.fail("Registration failed or did not redirect to the account page")

if __name__ == "__main__":
    unittest.main()