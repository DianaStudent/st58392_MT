import unittest
import time
import random
import string

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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the account icon/button.
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # 3. Select the "Register" option.
        register_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/register']")))
        register_link.click()

        # 4. Wait for the registration page to load.
        register_heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']")))
        self.assertIsNotNone(register_heading, "Registration page did not load.")

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)

        repeat_password_field = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
        repeat_password_field.send_keys(password)

        firstname_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        firstname_field.send_keys(firstname)

        lastname_field = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/../option[2]")))
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/../option[2]")))
        ActionChains(driver).move_to_element(state_dropdown).click().perform()
        state_dropdown.click()

        # 8. Submit the form.
        register_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button/span[text()='Register']/..")))
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        wait.until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url, "Registration failed. Redirected URL does not contain '/my-account'.")


if __name__ == "__main__":
    unittest.main()