import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account icon/button.
        try:
            account_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or not clickable: {e}")

        # 3. Select the "Register" option.
        try:
            register_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found or not clickable: {e}")

        # 4. Wait for the registration page to load.
       # Implicitly done by the following waits

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        try:
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)

            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)

            repeat_password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)

            firstname_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            firstname_field.send_keys(firstname)

            lastname_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            lastname_field.send_keys(lastname)

        except Exception as e:
            self.fail(f"One or more registration fields not found: {e}")

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        try:
            country_dropdown = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
            )
            select_country = Select(country_dropdown)
            select_country.select_by_index(1)  # Select the first country

        except Exception as e:
            self.fail(f"Country dropdown not found or not selectable: {e}")

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        try:
            state_dropdown = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
            )

            # Click outside the dropdown to ensure it closes
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element(By.CLASS_NAME, "login-register-area")).click().perform()

            select_state = Select(state_dropdown)
            select_state.select_by_index(1)  # Select the first state

        except Exception as e:
            self.fail(f"State dropdown not found or not selectable: {e}")

        # 8. Submit the form.
        try:
            register_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {e}")

        # 9. Wait for the page to redirect and confirm registration success.
        try:
            self.wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", self.driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed or redirect to /my-account failed: {e}")

if __name__ == "__main__":
    unittest.main()