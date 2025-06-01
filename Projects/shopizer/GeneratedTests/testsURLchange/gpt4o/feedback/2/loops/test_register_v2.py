import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterUserTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver using WebDriver Manager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        
    def generate_random_email(self):
        # Generate a random email
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get("http://localhost/")

        # Step 2: Click on the account icon/button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        # Step 3: Select the "Register" option
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 4: Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-register-area")))

        # Step 5: Fill in all fields: email, password, repeat password, first name, last name
        email = self.generate_random_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        password = "test**11"
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Step 6: Select a first country from the dropdown
        country_select = driver.find_element(By.XPATH, "//select[option='Select a country']")
        country_select.click()
        country_options = country_select.find_elements(By.TAG_NAME, "option")
        if not country_options:
            self.fail("Country options missing")
        country_options[1].click()

        # Step 7: Select a first state only after selecting country
        state_select = driver.find_element(By.XPATH, "//select[option='Select a state']")
        state_select.click()
        state_options = state_select.find_elements(By.TAG_NAME, "option")
        if not state_options:
            self.fail("State options missing")
        state_options[1].click()

        # Click somewhere else to close the dropdown
        driver.find_element(By.NAME, "lastName").click()

        # Step 8: Submit the form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        # Step 9: Confirm registration success
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Registration failed, not redirected to /my-account")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()