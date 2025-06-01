from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage (already done in setUp)

        # 2. Click the "Register" link in the top navigation.
        try:
            register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            register_link.click()
        except NoSuchElementException:
            self.fail("Register link not found.")
        except Exception as e:
            self.fail(f"Error clicking register link: {e}")

        # 3. Wait for the registration form to load.
        try:
            register_form_title = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Register']")))
        except NoSuchElementException:
            self.fail("Registration form title not found.")
        except Exception as e:
            self.fail(f"Error waiting for registration form: {e}")

        # 4. Select the appropriate gender radio input based on the provided data.
        try:
            female_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            female_radio.click()
        except NoSuchElementException:
            self.fail("Female gender radio button not found.")
        except Exception as e:
            self.fail(f"Error selecting gender: {e}")

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        try:
            first_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "FirstName")))
            last_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "LastName")))
            email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Email")))
            company_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Company")))
            password_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Password")))
            confirm_password_input = self.wait.until(EC.element_to_be_clickable((By.ID, "ConfirmPassword")))

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            email_input.send_keys(f"test.user{time.time()}@example.com")
            company_input.send_keys("TestCorp")
            password_input.send_keys("test11")
            confirm_password_input.send_keys("test11")

        except NoSuchElementException:
            self.fail("One or more input fields not found.")
        except Exception as e:
            self.fail(f"Error filling in form fields: {e}")

        # 6. Submit the registration form.
        try:
            register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except NoSuchElementException:
            self.fail("Register button not found.")
        except Exception as e:
            self.fail(f"Error submitting registration form: {e}")

        # 7. Wait for the response page or confirmation message to load.
        try:
            confirmation_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        except NoSuchElementException:
            self.fail("Confirmation message element not found.")
        except Exception as e:
            self.fail(f"Error waiting for confirmation message: {e}")

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        try:
            confirmation_text = confirmation_message.text
            self.assertIn("Your registration completed", confirmation_text, "Registration confirmation message is incorrect.")
        except AttributeError:
            self.fail("Confirmation message text is empty.")
        except Exception as e:
            self.fail(f"Error verifying confirmation message: {e}")

if __name__ == "__main__":
    unittest.main()