import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Accept cookies
        cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        cookie_button.click()

        # Open account menu
        account_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        # Click Register
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for registration page
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

        # Fill in registration form
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        first_name_input = driver.find_element(By.NAME, "firstName")
        last_name_input = driver.find_element(By.NAME, "lastName")

        # Generate a random email
        random_email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

        email_input.send_keys(random_email)
        password_input.send_keys("test**11")
        repeat_password_input.send_keys("test**11")
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")

        # Select country
        country_dropdown = Select(driver.find_element(By.XPATH, "//select[option='Select a country']"))
        country_dropdown.select_by_visible_text("Canada")

        # To ensure dropdown changes, click to another place
        actions = ActionChains(driver)
        actions.move_by_offset(10, 10).click().perform()

        # Wait for regions to populate and select region
        state_dropdown = Select(driver.find_element(By.XPATH, "//select[option='Select a state']"))
        state_dropdown.select_by_visible_text("Quebec")

        # Submit form
        submit_button = driver.find_element(By.XPATH, "//button[span='Register']")
        submit_button.click()

        # Wait for redirection to my-account
        self.wait.until(EC.url_contains("/my-account"))

        # Confirm success by checking URL
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Registration did not redirect to /my-account")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()