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
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test**11"
        self.firstname = "Test"
        self.lastname = "User"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
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
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        register_form = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
        firstname_field = driver.find_element(By.NAME, "firstName")
        lastname_field = driver.find_element(By.NAME, "lastName")

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        repeat_password_field.send_keys(self.password)
        firstname_field.send_keys(self.firstname)
        lastname_field.send_keys(self.lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = driver.find_element(By.XPATH, "//select/option[text()='Select a country']/../option[2]")
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = driver.find_element(By.XPATH, "//select/option[text()='Select a state']/../option[2]")
        ActionChains(driver).move_to_element(state_dropdown).click(state_dropdown).perform()

        # 8. Submit the form.
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
        )
        submit_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)


if __name__ == "__main__":
    unittest.main()