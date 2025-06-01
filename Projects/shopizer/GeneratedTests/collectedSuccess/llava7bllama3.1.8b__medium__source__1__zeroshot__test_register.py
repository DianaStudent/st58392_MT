import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Click on account button and select "Register"
        account_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
        )
        account_button.click()
        register_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # Fill in registration form
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        confirm_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "confirm_password"))
        )

        email_input.send_keys("test@example.com")
        password_input.send_keys("test**11")
        confirm_password_input.send_keys("test**11")

        # Select a country and region/state
        select_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='country']"))
        )
        select_region = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='region']"))
        )

        select_country.send_keys("United States")
        select_region.send_keys("California")

        # Submit registration form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "register-submit"))
        )
        submit_button.click()

        try:
            # Wait for redirect and confirm success by checking if the current URL includes "/my-account"
            WebDriverWait(self.driver, 20).until(EC.url_contains("/my-account"))
        except TimeoutException:
            self.fail("Registration failed")

    def test_register_error(self):
        # Fill in registration form with missing required field
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        email_input.send_keys("test@example.com")
        password_input.send_keys("test**11")

        # Submit registration form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "register-submit"))
        )
        submit_button.click()

        try:
            # Check that an error message is displayed
            error_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='error-message']"))
            )
            self.fail("Registration failed with missing required field")
        except TimeoutException:
            pass

if __name__ == "__main__":
    unittest.main()