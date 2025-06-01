from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_registration(self):
        # Open the homepage
        self.driver.get("http://max/")

        # Click the "Register" link
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration page to load
        WebDriverWait(self.driver, 20).until(EC.title_contains("Sign Up"))

        # Fill all the fields
        gender_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "gender-female")))
        gender_checkbox.click()

        first_name_input = self.driver.find_element(By.NAME, "first_name")
        first_name_input.send_keys("Test")

        last_name_input = self.driver.find_element(By.NAME, "last_name")
        last_name_input.send_keys("User")

        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        email_input.send_keys("testuser@example.com")

        company_input = self.driver.find_element(By.NAME, "company")
        company_input.send_keys("TestCorp")

        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.send_keys("test11")

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Verify that a message like "Your registration completed" is shown after successful registration
        success_message_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertIsNotNone(success_message_element)
        self.assertNotEqual(success_message_element.text.strip(), "")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()