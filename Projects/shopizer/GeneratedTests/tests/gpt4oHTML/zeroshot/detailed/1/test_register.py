import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{suffix}@user.com"

    def test_register(self):
        driver = self.driver
        wait = self.wait

        # Open the home page
        driver.get("http://localhost:8080")

        # Accept cookies if the button is present
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass  # If the cookie button is not present, ignore it

        # Step 2: Click on the account icon/button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Step 3: Select the "Register" option
        register_link = wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[@href='/register']")))
        register_link.click()

        # Step 4: Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-register-form")))

        # Step 5: Fill in all fields
        email = self.generate_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Step 6: Select a first country from the dropdown
        country_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='']")))  # Assuming no name attribute
        first_country_option = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='CA']")))
        first_country_option.click()

        # Wait after clicking to ensure region/states are visible
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='']")))  # State dropdown

        # Step 7: Select the first state after selecting a country
        state_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='']")  # Assuming no name attribute
        first_state_option = state_dropdown.find_element(By.XPATH, "//option[@value='QC']")
        first_state_option.click()

        # Click outside to close the dropdown
        driver.find_element(By.TAG_NAME, "body").click()

        # Step 8: Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        submit_button.click()

        # Step 9: Wait for the page to redirect and confirm registration success
        wait.until(EC.url_contains("/my-account"))

        current_url = driver.current_url
        if "/my-account" not in current_url:
            self.fail("Registration was not successful - did not navigate to '/my-account'.")

        # Confirm welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-profile .user-name")))
        self.assertIn("Welcome Test User", welcome_message.text, "The welcome message is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()