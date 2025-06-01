import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import uuid

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Find and click the 'Register' link.  Since it's not directly provided in the HTML,
        # we'll assume it's in the header and use a general link selector.
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except NoSuchElementException:
            self.fail("Register link not found.")

        # Verify that we are on the registration page
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
        )

        # Generate a unique email
        unique_id = str(uuid.uuid4())
        email = f"test_{unique_id}@example.com"

        # Locate the elements and fill the registration form
        try:
            male_gender_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            male_gender_radio.click()

            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)

            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Acme Corp")

            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "Newsletter"))
            )
            # Ensure the checkbox is checked.
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")

            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")

            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()

        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except Exception as e:
            self.fail(f"An error occurred during form filling: {e}")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )
            result_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue("Your registration completed" in result_message.text)

        except NoSuchElementException:
            self.fail("Registration result message not found.")
        except Exception as e:
            self.fail(f"An error occurred while verifying registration: {e}")

if __name__ == "__main__":
    unittest.main()