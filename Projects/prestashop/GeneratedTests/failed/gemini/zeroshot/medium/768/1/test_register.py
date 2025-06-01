from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click on the login link
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 2. Click on the registration link
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Registration link not found")

        # 3. Fill in the registration form
        gender_mr_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        if gender_mr_radio:
            gender_mr_radio.click()
        else:
            self.fail("Gender Mr. radio button not found")

        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if first_name_input:
            first_name_input.send_keys("Test")
        else:
            self.fail("First name input not found")

        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if last_name_input:
            last_name_input.send_keys("User")
        else:
            self.fail("Last name input not found")

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_input:
            email_input.send_keys(self.email)
        else:
            self.fail("Email input not found")

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_input:
            password_input.send_keys(self.password)
        else:
            self.fail("Password input not found")

        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys("01/01/2000")
        else:
            self.fail("Birthday input not found")

        # 4. Check required checkboxes
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("psgdpr checkbox not found")

        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("customer_privacy checkbox not found")

        # 5. Submit the form
        save_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 6. Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
        )

        if sign_out_link and sign_out_link.text == "Sign out":
            pass  # Success!
        else:
            self.fail("Sign out link not found after registration")

if __name__ == "__main__":
    unittest.main()