import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import string
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_and_login(self):
        driver = self.driver
        wait = self.wait

        # Open the home page
        driver.get("http://localhost/")  # Replace with the actual URL

        # Accept cookies if the dialog is present
        try:
            cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookies_button.click()
        except:
            pass  # Continue if the cookies dialog is not present

        # Click on the account icon/button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Select the "Register" option
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in the registration form
        email_address = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
        password = "test**11"

        driver.find_element(By.NAME, "email").send_keys(email_address)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select the first country
        country_select = Select(driver.find_element(By.TAG_NAME, "select"))
        country_select.select_by_index(1)  # Assuming index 0 is "Select a country"

        # Click on some place to avoid hiding the state dropdown
        driver.find_element(By.TAG_NAME, "body").click()

        # Select the first state
        state_select = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select[2]"))))
        state_select.select_by_index(1)  # Assuming index 0 is "Select a state"

        # Submit the registration form
        driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']").click()

        # Wait for the page to redirect and confirm registration success
        wait.until(EC.url_contains("/my-account"))

        # Validate that registration was successful
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, f"Expected URL to contain '/my-account', but got: {current_url}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()