import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegistration(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080")

    def test_register_account(self):
        # Click on the account icon/button
        account_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='account']")))
        account_button.click()

        # Select the "Register" option
        register_option = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/register']")))
        register_option.click()

        # Wait for the registration page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2:contains('Register')")))

        # Fill in all fields
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='email']")))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        repeat_password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='repeatPassword']")))
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='firstName']")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='lastName']")))

        email_input.send_keys(f"test_xxxxxx@user.com")
        password_input.send_keys("test**11")
        repeat_password_input.send_keys("test**11")
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")

        # Select a country
        country_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='country']")))
        country_dropdown.click()

        # Select a state
        state_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-name='state']")))
        state_dropdown.click()

        # Submit the form
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))
        submit_button.click()

        # Wait for the page to redirect and confirm registration success
        WebDriverWait(self.driver, 20).until(EC.url_contains("/my-account"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()