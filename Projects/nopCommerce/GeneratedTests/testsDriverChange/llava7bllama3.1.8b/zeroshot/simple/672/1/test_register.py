import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_registration(self):
        # Get email and password dynamically
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']")))
        email_input.send_keys('test@example.com')
        
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']")))
        password_input.send_keys('test11')

        # Fill all registration fields
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='FirstName']")))
        first_name_input.send_keys('Test Name')
        
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='LastName']")))
        last_name_input.send_keys('Test Last')

        confirm_password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='ConfirmPassword']")))
        confirm_password_input.send_keys('test11')

        # Submit registration form
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='register-next-step-button']")))
        register_button.click()

        # Check for successful registration message
        result_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertEqual(result_message.text, 'Your registration completed')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()