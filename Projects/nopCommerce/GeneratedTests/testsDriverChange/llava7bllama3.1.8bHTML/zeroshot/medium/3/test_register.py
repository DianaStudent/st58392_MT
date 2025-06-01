import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_register(self):
        self.driver.get(html_data["home_before_register"])
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button-1")))
        register_button.click()

        # Wait for the registration page to load
        registration_page_loaded = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'register-button')))
        self.assertIsNotNone(registration_page_loaded)

        # Fill all fields
        gender_male = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Male']")))
        self.assertEqual(gender_male.get_attribute('value'), "Male")
        gender_female = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-female']")))
        gender_female.click()
        
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'first-name')))
        self.assertIsNotNone(first_name_input)
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'last-name')))
        self.assertIsNotNone(last_name_input)
        last_name_input.send_keys("User")

        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        self.assertIsNotNone(email_input)
        email_input.send_keys("test@example.com")

        company_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'company')))
        self.assertIsNotNone(company_input)
        company_input.send_keys("TestCorp")

        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'Password')))
        self.assertIsNotNone(password_input)
        password_input.send_keys("test11")

        confirm_password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'ConfirmPassword')))
        self.assertIsNotNone(confirm_password_input)
        confirm_password_input.send_keys("test11")

        # Submit the registration form
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.register-next-step-button")))
        register_button.click()

        # Verify that a message like "Your registration completed" is shown after successful registration
        registration_complete_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertIsNotNone(registration_complete_message)
        self.assertIn("Your registration completed", registration_complete_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()