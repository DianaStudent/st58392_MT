import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterUserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        
    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        driver.get("http://localhost/")

        # Accept cookies if the button is present
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass

        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Ensure registration form is loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-register-area")))

        # Generate email and fill out the form
        email = self.generate_random_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        password = "test**11"
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Selecting country and state
        country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
        country_select.click()
        country_option = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='CA']")))
        country_option.click()

        state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
        state_select.click()
        state_option = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='QC']")))
        state_option.click()

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        # Validate successful registration
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Registration failed, not redirected to /my-account")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()