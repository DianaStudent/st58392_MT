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
        self.driver.get("http://max/")

    def test_register_user(self):
        # Click the "Register" button
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
        )
        register_button.click()

        # Fill all the fields on the registration page
        first_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "first_name")))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "last_name")))
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        company_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "company")))
        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        confirm_password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "confirm_password")))

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys("testuser" + str(1) + "@example.com") # dynamically generated
        company_field.send_keys("TestCorp")
        password_field.send_keys("test11")
        confirm_password_field.send_keys("test11")

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Verify that a message like "Your registration completed" is shown after successful registration
        result_message = WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element_value((By.XPATH, "//div[@class='result']"), "Your registration completed")
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()