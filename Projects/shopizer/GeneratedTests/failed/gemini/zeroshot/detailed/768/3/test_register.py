from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account icon/button.
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        register_heading = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']"))
        )
        self.assertIsNotNone(register_heading, "Registration page did not load.")

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

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

        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        last_name_field.send_keys(last_name)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../option[2]"))
        )
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../option[2]"))
        )
        state_dropdown.click()

        # Click some place to avoid country selector hide state selector
        ActionChains(self.driver).move_to_element(register_heading).click().perform()

        # 8. Submit the form.
        register_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
        )
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url, "Registration failed. Redirect URL does not contain '/my-account'.")


if __name__ == "__main__":
    unittest.main()