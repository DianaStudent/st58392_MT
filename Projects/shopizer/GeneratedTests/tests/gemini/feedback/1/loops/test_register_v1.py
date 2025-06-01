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

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # 2. Click on the account icon/button.
        account_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
        firstname_field = driver.find_element(By.NAME, "firstName")
        lastname_field = driver.find_element(By.NAME, "lastName")

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = driver.find_element(By.XPATH, "//select/option[text()='Select a country']/../option[2]")
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        time.sleep(1)
        state_dropdown = driver.find_element(By.XPATH, "//select/option[text()='Select a state']/../option[2]")
        state_dropdown.click()
        driver.find_element(By.CLASS_NAME, "login-register-wrapper").click()

        # 8. Submit the form.
        register_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Register']]"))
        )
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        wait.until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url)


if __name__ == "__main__":
    unittest.main()