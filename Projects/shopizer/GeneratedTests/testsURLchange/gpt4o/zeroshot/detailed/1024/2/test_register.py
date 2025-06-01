import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("http://localhost/")
        self.browser.maximize_window()

    def test_user_registration(self):
        browser = self.browser
        wait = WebDriverWait(browser, 20)

        # Click on the account icon/button
        account_icon_selector = (By.CLASS_NAME, "pe-7s-user-female")
        account_icon = wait.until(EC.presence_of_element_located(account_icon_selector))
        account_icon.click()

        # Select the "Register" option 
        register_option_selector = (By.LINK_TEXT, "Register")
        register_option = wait.until(EC.element_to_be_clickable(register_option_selector))
        register_option.click()

        # Wait for the registration page to load
        registration_form_selector = (By.CLASS_NAME, "login-register-form")
        wait.until(EC.presence_of_element_located(registration_form_selector))

        # Fill in all fields: email, password, repeat password, first name, last name
        email_input = browser.find_element(By.NAME, "email")
        password_input = browser.find_element(By.NAME, "password")
        repeat_password_input = browser.find_element(By.NAME, "repeatPassword")
        first_name_input = browser.find_element(By.NAME, "firstName")
        last_name_input = browser.find_element(By.NAME, "lastName")

        email = f"test_{int(time.time())}@user.com"
        password = "test**11"

        email_input.send_keys(email)
        password_input.send_keys(password)
        repeat_password_input.send_keys(password)
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")

        # Select a first country from the dropdown and wait for region/state dropdown to load
        country_dropdown = Select(browser.find_element(By.CSS_SELECTOR, ".login-input select"))
        country_dropdown.select_by_index(1)  # Selecting first option after the placeholder

        time.sleep(2)  # Wait for state dropdown to load. Replace with wait for state visibility if possible.

        # Select a state only after selecting country
        state_dropdown = Select(browser.find_elements(By.CSS_SELECTOR, ".login-input select")[1])
        state_dropdown.select_by_index(1)

        # To avoid country selector hiding state selector
        last_name_input.click()

        # Submit the form
        register_button_xpath = '//button/span[text()="Register"]/..'
        register_button = browser.find_element(By.XPATH, register_button_xpath)
        register_button.click()

        # Wait for the page to redirect and confirm registration success
        wait.until(EC.url_contains("/my-account"))

        # Assert that the redirected URL contains "/my-account"
        self.assertIn("/my-account", browser.current_url)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()