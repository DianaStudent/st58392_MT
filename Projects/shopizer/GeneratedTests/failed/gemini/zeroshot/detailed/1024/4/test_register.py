from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # 2. Click on the account icon/button.
        account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # 3. Select the "Register" option.
        register_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
        register_link.click()

        # 4. Wait for the registration page to load.
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']")))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password)

        repeat_password_field = self.driver.find_element(By.NAME, "repeatPassword")
        repeat_password_field.send_keys(password)

        firstname_field = self.driver.find_element(By.NAME, "firstName")
        firstname_field.send_keys(firstname)

        lastname_field = self.driver.find_element(By.NAME, "lastName")
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = self.driver.find_element(By.XPATH, "//select/option[text()='Select a country']/../option[2]")
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../option[2]")))
        state_dropdown.click()
        ActionChains(self.driver).move_by_offset(1, 1).click().perform()

        # 8. Submit the form.
        register_button = self.driver.find_element(By.XPATH, "//button[span[text()='Register']]")
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()