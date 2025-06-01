from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass

        # 2. Click on the account icon/button.
        account_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']")))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        repeat_password_field = wait.until(EC.element_to_be_clickable((By.NAME, "repeatPassword")))
        firstname_field = wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
        lastname_field = wait.until(EC.element_to_be_clickable((By.NAME, "lastName")))

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../.."))))
        country_select.select_by_index(1)

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../.."))))
        state_select.select_by_index(1)

        # Click on some place to avoid country selector hide state selector.
        driver.find_element(By.CLASS_NAME, "login-register-wrapper").click()

        # 8. Submit the form.
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']/..")))
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        wait.until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url)


if __name__ == "__main__":
    unittest.main()