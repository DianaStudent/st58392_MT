from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import random
import string

class RegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_register(self):
        driver = self.driver

        # Accept cookies
        cookie_accept_button = self.wait.until(EC.presence_of_element_located(
            (By.ID, "rcc-confirm-button")))
        cookie_accept_button.click()

        # Click on the account button/icon
        account_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        # Click on the 'Register' link
        register_link = self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration form to load
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in registration details
        email = self.generate_random_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select the first country ('Canada')
        country_dropdown = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select/option[@value='CA']")))
        country_dropdown.click()

        # Ensure that the state dropdown is interactable
        state_dropdown = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select/option[@value='QC']")))
        state_dropdown.click()

        # Click elsewhere to ensure state selection
        driver.find_element(By.TAG_NAME, "body").click()

        # Submit the registration form
        submit_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='button-box']/button[@type='submit']")))
        submit_button.click()

        # Wait for redirection to the account page
        self.wait.until(EC.url_contains("/my-account"))

        # Assert the URL contains '/my-account' to confirm successful registration
        self.assertIn("/my-account", driver.current_url, "Registration failed or didn't redirect to account page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()