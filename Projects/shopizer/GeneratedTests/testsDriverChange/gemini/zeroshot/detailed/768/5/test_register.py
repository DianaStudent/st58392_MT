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
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test**11"
        self.firstname = "Test"
        self.lastname = "User"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account icon/button.
        account_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']"))
        )

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(self.email)

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(self.password)

        repeat_password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        repeat_password_field.send_keys(self.password)

        first_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        first_name_field.send_keys(self.firstname)

        last_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        last_name_field.send_keys(self.lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
        )
        country_dropdown.click()
        country_option = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Canada']"))
        )
        country_option.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/parent::select"))
        )
        ActionChains(driver).move_to_element(state_dropdown).click().perform()
        state_option = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Quebec']"))
        )
        state_option.click()

        # 8. Submit the form.
        register_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button/span[text()='Register']/parent::button"))
        )
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        wait.until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url)


if __name__ == "__main__":
    unittest.main()