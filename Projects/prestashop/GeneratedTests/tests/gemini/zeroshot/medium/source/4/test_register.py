import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the login link in the top menu.
        sign_in_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 3. Click on the register link on the login page.
        create_account_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]"))
        )
        if create_account_link:
            create_account_link.click()
        else:
            self.fail("Create account link not found")

        # 4. Fill in the registration form fields:
        #    - Gender, First name, Last name, Email, Password, Birthday
        gender_mr_radio = wait.until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        if gender_mr_radio:
            gender_mr_radio.click()
        else:
            self.fail("Gender Mr. radio button not found")

        first_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if first_name_input:
            first_name_input.send_keys("Test")
        else:
            self.fail("First name input not found")

        last_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if last_name_input:
            last_name_input.send_keys("User")
        else:
            self.fail("Last name input not found")

        email = "test_" + str(random.randint(100000, 999999)) + "@user.com"
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_input:
            email_input.send_keys(email)
        else:
            self.fail("Email input not found")

        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_input:
            password_input.send_keys("test@user1")
        else:
            self.fail("Password input not found")

        birthday_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys("01/01/2000")
        else:
            self.fail("Birthday input not found")

        # 5. Check required checkboxes.
        psgdpr_checkbox = wait.until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("PSGDPR checkbox not found")

        customer_privacy_checkbox = wait.until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("Customer privacy checkbox not found")

        # 6. Submit the form.
        save_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//footer[@class='form-footer clearfix']/button[@type='submit']"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 7. Confirm success by checking for the presence of "Sign out" in the top bar.
        sign_out_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
        )

        if sign_out_link:
            self.assertEqual("Sign out", sign_out_link.text)
        else:
            self.fail("Sign out link not found after registration")

if __name__ == "__main__":
    unittest.main()