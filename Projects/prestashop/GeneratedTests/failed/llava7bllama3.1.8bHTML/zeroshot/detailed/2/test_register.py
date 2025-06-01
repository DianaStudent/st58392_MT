from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from email_validator import validate_email, EmailNotValidError

class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Register link
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='register']")))
        register_link.click()

        # Fill in credentials
        gender = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'id_gender1')))
        gender.click()
        
        first_name = self.driver.find_element(By.NAME, "first_name")
        first_name.send_keys("Test")

        last_name = self.driver.find_element(By.NAME, "last_name")
        last_name.send_keys("User")

        # Generate dynamic email
        try:
            email = validate_email(f"test_{self.get_random_string(8)}@user.com", check_deliverability=False)
            email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
            email_input.send_keys(email.address)

            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("test@user1")

            birthday = self.driver.find_element(By.NAME, "birthday")
            birthday.send_keys("01/01/2000")

        except EmailNotValidError as e:
            self.fail(f"Invalid email address: {e}")

        # Ticking checkboxes
        privacy_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'optin')))
        privacy_checkbox.click()

        newsletter_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'newsletter')))
        newsletter_checkbox.click()

        terms_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'optin')))
        terms_checkbox.click()

        # Submit form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit")))
        submit_button.click()

        # Wait for redirect after login
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))

        # Assert success
        sign_out_button = self.driver.find_element(By.LINK_TEXT, "Sign out")
        username_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'header_logo'))).text

    def get_random_string(self, length):
        import random
        characters = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    unittest.main()