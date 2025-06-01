from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Replace with the actual URL

    def test_register_new_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {str(e)}")

        # Navigate to the register page
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {str(e)}")

        # Fill in registration form
        try:
            email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
            wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
            driver.find_element(By.NAME, "password").send_keys("test**11")
            driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
            driver.find_element(By.NAME, "firstName").send_keys("Test")
            driver.find_element(By.NAME, "lastName").send_keys("User")

            # Select Country and State from dropdowns
            country_select = driver.find_elements(By.TAG_NAME, "select")[0]
            country_options = country_select.find_elements(By.TAG_NAME, "option")
            country_options[1].click()  # Assuming 1 is Canada

            state_select = driver.find_elements(By.TAG_NAME, "select")[1]
            state_options = state_select.find_elements(By.TAG_NAME, "option")
            state_options[1].click()  # Assuming 1 is Quebec

            # Submit form
            driver.find_elements(By.CSS_SELECTOR, ".button-box button")[0].click()

        except Exception as e:
            self.fail(f"Failed to fill and submit the registration form: {str(e)}")

        # Verify successful registration by URL redirection
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"URL did not redirect to /my-account: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()