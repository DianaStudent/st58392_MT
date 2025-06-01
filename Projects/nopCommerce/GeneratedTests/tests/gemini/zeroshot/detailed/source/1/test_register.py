import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click the "Register" link in the top navigation.
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 3. Wait for the registration form to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
        )

        # 4. Select the appropriate gender radio input based on the provided data.
        female_gender_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "gender-female"))
        )
        female_gender_radio.click()

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "FirstName"))
        )
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "LastName"))
        )
        last_name_input.send_keys("User")

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        email = "testuser_" + str(uuid.uuid4()) + "@example.com"
        email_input.send_keys(email)

        company_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Company"))
        )
        company_input.send_keys("TestCorp")

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        password_input.send_keys("test11")

        confirm_password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ConfirmPassword"))
        )
        confirm_password_input.send_keys("test11")

        # 6. Submit the registration form.
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )
        register_button.click()

        # 7. Wait for the response page or confirmation message to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
        )

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        confirmation_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "result"))
        )

        if confirmation_message_element:
            confirmation_message_text = confirmation_message_element.text
            if confirmation_message_text:
                self.assertIn("Your registration completed", confirmation_message_text)
            else:
                self.fail("Confirmation message text is empty.")
        else:
            self.fail("Confirmation message element is not found.")

if __name__ == "__main__":
    unittest.main()