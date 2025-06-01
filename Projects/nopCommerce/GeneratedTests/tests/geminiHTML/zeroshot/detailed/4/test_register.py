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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the "Register" link in the top navigation.
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # 3. Wait for the registration form to load.
        register_form_title = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Register']")))
        self.assertEqual(register_form_title.text, "Register")

        # 4. Select the appropriate gender radio input based on the provided data.
        gender = "F"
        gender_female_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_male_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-male")))

        if gender == "F":
            gender_female_radio.click()
        elif gender == "M":
            gender_male_radio.click()
        else:
            self.fail("Invalid gender specified.")

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name = "Test"
        last_name = "User"
        email = f"testuser_{uuid.uuid4()}@example.com"
        company = "TestCorp"
        password = "test11"

        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        company_input = self.wait.until(EC.presence_of_element_located((By.ID, "Company")))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "Password")))
        confirm_password_input = self.wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        company_input.send_keys(company)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

        # 6. Submit the registration form.
        register_button = self.wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        register_button.click()

        # 7. Wait for the response page or confirmation message to load.
        confirmation_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        if confirmation_message:
            self.assertIn("Your registration completed", confirmation_message.text)
        else:
            self.fail("Confirmation message is missing.")

if __name__ == "__main__":
    unittest.main()