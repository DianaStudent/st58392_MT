import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def generate_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{random_string}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the button exists
        try:
            accept_cookies = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if accept_cookies:
                accept_cookies.click()
        except:
            pass
        
        # Click on the account icon/button
        account_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_icon.click()

        # Select the "Register" option
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in the form fields
        email = self.generate_email()
        password = "test**11"
        
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select the first country and state from dropdowns
        country_select = driver.find_element(By.TAG_NAME, "select")
        country_select.click()
        country_options = country_select.find_elements(By.TAG_NAME, "option")
        assert len(country_options) > 0, self.fail("No countries available in dropdown.")
        country_options[1].click()
        
        # Click to avoid country selector hiding
        ActionChains(driver).move_by_offset(100, 100).click().perform()
        time.sleep(1)  # Give time for the state selector to load

        state_select = driver.find_element(By.TAG_NAME, "select")
        state_options = state_select.find_elements(By.TAG_NAME, "option")
        assert len(state_options) > 0, self.fail("No states available in dropdown.")
        state_options[1].click()

        # Submit the form
        driver.find_element(By.XPATH, "//form//button").click()

        # Wait for the page redirection and confirm registration success
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url, "Failed to reach My Account page after registration.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()