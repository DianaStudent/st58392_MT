import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Accept cookies
        cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # Step 2: Click on account icon/button
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Step 3: Select the "Register" option
        register_option = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_option.click()

        # Step 4: Wait for the registration page to load
        register_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-register-form")))

        # Generate a dynamic email
        email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

        # Step 5: Fill in the registration form
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Step 6: Select a country
        country_dropdown = driver.find_element(By.XPATH, "//select/option[@value='CA']")
        country_dropdown.click()

        # Step 7: Select a state
        state_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[@value='QC']")))
        state_dropdown.click()

        # Click elsewhere to ensure dropdown selections close
        driver.find_element(By.XPATH, "//h4[text()=' Register']").click()

        # Step 8: Submit the form
        driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']").click()

        # Step 9: Verify registration success
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail("User registration failed: not redirected to /my-account.")

if __name__ == "__main__":
    unittest.main()