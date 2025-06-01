from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # 1. Click on the login link in the top menu
        sign_in_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 2. Click on the register link on the login page
        create_account_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]"))
        )
        if create_account_link:
            create_account_link.click()
        else:
            self.fail("Create account link not found")

        # 3. Fill in the registration form fields
        # Generate a random email
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        password = "test@user1"

        # Select gender
        mr_radio = wait.until(
            EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
        )
        if mr_radio:
            mr_radio.click()
        else:
            self.fail("Mr. radio button not found")

        # Fill in first name
        firstname_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if firstname_field:
            firstname_field.send_keys("Test")
        else:
            self.fail("First name field not found")

        # Fill in last name
        lastname_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if lastname_field:
            lastname_field.send_keys("User")
        else:
            self.fail("Last name field not found")

        # Fill in email
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_field:
            email_field.send_keys(email)
        else:
            self.fail("Email field not found")

        # Fill in password
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_field:
            password_field.send_keys(password)
        else:
            self.fail("Password field not found")

        # Fill in birthday
        birthday_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_field:
            birthday_field.send_keys("01/01/2000")
        else:
            self.fail("Birthday field not found")

        # 4. Check required checkboxes
        psgdpr_checkbox = wait.until(
            EC.element_to_be_clickable((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("GDPR checkbox not found")

        customer_privacy_checkbox = wait.until(
            EC.element_to_be_clickable((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("Customer privacy checkbox not found")

        # 5. Submit the form
        save_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 6. Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
        )

        if sign_out_link and sign_out_link.text == "Sign out":
            pass  # Success!
        else:
            self.fail("Sign out link not found after registration")

if __name__ == "__main__":
    unittest.main()