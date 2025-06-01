import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email_prefix = "test_" + str(uuid.uuid4().hex[:6]) + "@user.com"
        self.credentials = {
            "gender": "1",
            "firstname": "Test",
            "lastname": "User",
            "email": self.email_prefix,
            "password": "test@user1",
            "birthday": "01/01/2000"
        }

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']/div/a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        create_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()

        # 4. Fill in the registration form.
        gender_male_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_male_radio.click()

        firstname_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname_input.send_keys(self.credentials["firstname"])

        lastname_input = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname_input.send_keys(self.credentials["lastname"])

        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys(self.credentials["email"])

        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys(self.credentials["password"])

        birthday_input = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_input.send_keys(self.credentials["birthday"])

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        psgdpr_checkbox.click()

        customer_privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        save_button.click()

        # 7. Wait for the redirect after login.
        wait.until(EC.url_contains("http://localhost:8080/en/"))

        # 8. Confirm that login was successful.
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))
        sign_out_text = sign_out_link.text
        if not sign_out_text:
            self.fail("Sign out link text is empty")
        self.assertEqual(sign_out_text, "Sign out")

        username_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]")))
        username_text = username_link.text
        if not username_text:
            self.fail("Username link text is empty")
        self.assertEqual(username_text, "Test User")

if __name__ == "__main__":
    unittest.main()