from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
    
    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://localhost/")
        
        # Accept cookies
        accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies.click()

        # Step 2: Click on the account icon/button
        account_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # Step 3: Select the "Register" option
        register_option = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Register")))
        register_option.click()

        # Step 4: Wait for the registration page to load
        email_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, "email")))

        # Step 5: Fill in all fields
        email = self.generate_random_email()
        password = "test**11"
        
        email_input.send_keys(email)
        
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        
        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_input.send_keys(password)
        
        first_name_input = driver.find_element(By.NAME, "firstName")
        first_name_input.send_keys("Test")
        
        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys("User")
        
        # Step 6: Select the first country from the dropdown
        country_select = driver.find_element(By.XPATH, "//select[@name='country']")
        country_select.click()
        first_country_option = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//select[@name='country']/option[2]")))
        first_country_option.click()
        
        # Step 7: Select the first state
        state_select = driver.find_element(By.XPATH, "//select[@name='state']")
        state_select.click()
        first_state_option = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//select[@name='state']/option[2]")))
        first_state_option.click()
        
        # Ensure dropdowns are collapsed by clicking outside
        driver.find_element(By.TAG_NAME, "body").click()

        # Step 8: Submit the form
        register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()
        
        # Step 9: Confirm registration success
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()