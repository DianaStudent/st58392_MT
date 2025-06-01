import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the homepage. Already done in setUp

        # 2. Click the "Register" link in the top navigation.
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' link: {e}")

        # 3. Wait for the registration form to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
        except Exception as e:
            self.fail(f"Registration form did not load: {e}")

        # 4. Select the appropriate gender radio input based on the provided data.
        try:
            female_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-female"))
            )
            female_radio.click()
        except Exception as e:
            self.fail(f"Could not find or click the female gender radio button: {e}")

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            email = str(uuid.uuid4()) + "@example.com"
            email_input.send_keys(email)
            company_input.send_keys("TestCorp")
            password_input.send_keys("test11")
            confirm_password_input.send_keys("test11")

        except Exception as e:
            self.fail(f"Could not find or fill in the input fields: {e}")

        # 6. Submit the registration form.
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' button: {e}")

        # 7. Wait for the response page or confirmation message to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )
        except Exception as e:
            self.fail(f"Registration result page did not load: {e}")

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        try:
            confirmation_message_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            confirmation_message_text = confirmation_message_element.text
            self.assertIn("Your registration completed", confirmation_message_text)
        except Exception as e:
            self.fail(f"Confirmation message is missing or incorrect: {e}")


if __name__ == "__main__":
    unittest.main()