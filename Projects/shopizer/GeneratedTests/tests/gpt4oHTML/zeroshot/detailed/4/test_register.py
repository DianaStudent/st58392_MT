from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import random
import string

class RegisterProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080")  # Replace with the actual URL

    def test_register_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        # This is already done in setUp.

        # Step 2: Click on the account icon/button
        account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_icon.click()

        # Step 3: Select the "Register" option
        register_option = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_option.click()

        # Step 4: Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-register-wrapper")))

        # Prepare dynamic email
        email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"test_{email_prefix}@user.com"

        # Step 5: Fill in all fields
        self.fill_registration_form(driver, email)

        # Step 6: Select the first country from the dropdown
        country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='country']")))
        country_select.click()
        country_options = country_select.find_elements(By.TAG_NAME, "option")
        first_country = country_options[1]  # Assuming the first option is a placeholder
        first_country.click()

        # Step 7: Select a first state after selecting country
        state_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='state']")))
        state_select.click()
        state_options = state_select.find_elements(By.TAG_NAME, "option")
        first_state = state_options[1]  # Assuming the first option is a placeholder
        first_state.click()

        # Step 8: Submit the form
        submit_btn = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        submit_btn.click()

        # Step 9: Confirm registration success by checking if URL contains "/my-account"
        wait.until(EC.url_contains("/my-account"))

    def fill_registration_form(self, driver, email):
        # Fill email
        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(email)

        # Fill password
        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys("test**11")

        # Fill repeat password
        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repeatPassword']")
        repeat_password_input.send_keys("test**11")

        # Fill first name
        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
        first_name_input.send_keys("Test")

        # Fill last name
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
        last_name_input.send_keys("User")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()