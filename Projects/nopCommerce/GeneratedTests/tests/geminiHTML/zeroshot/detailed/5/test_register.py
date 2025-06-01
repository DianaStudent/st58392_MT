import unittest
import time
import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)
        driver = self.driver
        wait = self.wait

        # 2. Click the "Register" link in the top navigation.
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        register_link.click()

        # 3. Wait for the registration form to load.
        register_form_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Register']")))
        self.assertIsNotNone(register_form_title, "Registration form title not found.")

        # 4. Select the appropriate gender radio input based on the provided data.
        gender_female_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_female_radio.click()

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        company_input = wait.until(EC.presence_of_element_located((By.ID, "Company")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email = "testuser_" + str(uuid.uuid4()) + "@example.com"
        email_input.send_keys(email)
        company_input.send_keys("TestCorp")
        password_input.send_keys("test11")
        confirm_password_input.send_keys("test11")

        # 6. Submit the registration form.
        register_button = wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        register_button.click()

        # 7. Wait for the response page or confirmation message to load.
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        if confirmation_message:
            confirmation_text = confirmation_message.text
            self.assertIn("Your registration completed", confirmation_text, "Registration confirmation message not found.")
        else:
            self.fail("Confirmation message element not found.")


if __name__ == "__main__":
    unittest.main()