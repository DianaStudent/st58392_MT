from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_register(self):
        driver = self.driver

        # Step 1: Open the home page.
        driver.get("http://localhost/")  # replace with the actual home page URL

        # Step 2: Click on the account icon/button.
        account_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Step 3: Select the "Register" option.
        register_option = self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Register")))
        register_option.click()

        # Step 4: Wait for the registration page to load.
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='login-register-form']//input[@name='email']")))

        # Step 5: Fill in all fields: email, password, repeat password, first name, last name.
        random_email_suffix = random.randint(100000, 999999)
        email = f"test_{random_email_suffix}@user.com"
        
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys(email)

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("test**11")

        repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_field.send_keys("test**11")

        first_name_field = driver.find_element(By.NAME, "firstName")
        first_name_field.send_keys("Test")

        last_name_field = driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys("User")

        # Step 6: Select a first country from the dropdown and wait for region/state dropdown to load.
        country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
        country_select.click()
        country_select.send_keys(Keys.DOWN + Keys.RETURN)

        # Wait for state dropdown to be populated
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[option[text()='Select a state']]")))

        # Step 7: Select a first state only after selecting country
        state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
        state_select.click()
        state_select.send_keys(Keys.DOWN + Keys.RETURN)
        
        # Additional click to avoid dropdown interference
        driver.find_element(By.TAG_NAME, "body").click()

        # Step 8: Submit the form.
        register_button = driver.find_element(By.XPATH, "//button[span[text()='Register']]")
        register_button.click()

        # Step 9: Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        if "/my-account" not in current_url:
            self.fail(f"Registration failed. URL after registration: {current_url}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()