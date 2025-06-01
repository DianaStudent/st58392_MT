from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # replace with your actual homepage URL
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='register']")))

    def test_register(self):
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='register']")))
        register_button.click()

        # Wait for the registration form to load
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "register-button")))

        # Select the appropriate gender radio input based on the provided data.
        female_radio = self.driver.find_element(By.XPATH, "//input[@value='Female']")
        female_radio.click()

        # Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "first_name")))
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "last_name")))
        last_name_input.send_keys("User")

        email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # Dynamically generate the email.
        import uuid
from selenium.webdriver.chrome.service import Service as ChromeService
        email_value = f"test{uuid.uuid4().hex}@example.com"
        email_input.send_keys(email_value)

        company_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "company")))
        company_input.send_keys("TestCorp")

        password_input = self.driver.find_element(By.XPATH, "//input[@id='Password']")
        password_input.send_keys("test11")

        confirm_password_input = self.driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
        confirm_password_input.send_keys("test11")

        # Submit the registration form.
        register_button.click()

        # Wait for the response page or confirmation message to load
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "register-button")))

        # Verify that registration succeeded by checking:
        confirm_text = self.driver.find_element(By.XPATH, "//div[@class='result']")
        self.assertIsNotNone(confirm_text.text)
        self.assertIn("Your registration completed", confirm_text.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()