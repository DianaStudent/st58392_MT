from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = driver
        driver.get("http://max/")
    
    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Check if the 'Simple Registration' tab is visible
        registration_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='register-1']")))
        self.assertTrue(r"Simple Registration".encode('utf-8') in registration_tab.get_attribute("aria-label").encode('utf-8'))

        # Fill out the registration form
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='email']")))
        self.email_field = email_field
        email_field.send_keys(f"test11-{time.time()}@example.com")
        first_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='firstName']")))
        self.first_name_field = first_name_field
        first_name_field.send_keys("First name")
        last_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='lastName']")))
        self.last_name_field = last_name_field
        last_name_field.send_keys("Last name")
        date_of_birth_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='dateOfBirth']")))
        self.date_of_birth_field = date_of_birth_field
        date_of_birth_field.send_keys("1990-01-01")
        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='password']")))
        self.password_field = password_field
        password_field.send_keys("test11")
        confirm_password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='confirmPassword']")))
        self.confirm_password_field = confirm_password_field
        confirm_password_field.send_keys("test11")

        # Check if the 'Next Step' button is visible and click it to proceed to the next step of registration
        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='nextStep']")))
        self.next_button = next_button
        next_button.send_keys(Keys.RETURN)

        # Check if the 'Simple Registration' tab is visible again after clicking the 'Next Step' button
        registration_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='register-2']")))
        self.assertTrue(r"Simple Registration".encode('utf-8') in registration_tab.get_attribute("aria-label").encode('utf-8'))

        # Proceed to the next step of registration
        if 'registration' not in self.email_field.get_attribute('data-val'):
            self.fail("The email field is empty")

        # Check if the 'Simple Registration' tab is visible again for the last time after clicking the 'Next Step' button one last time
        registration_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='register-3']")))
        self.assertTrue(r"Simple Registration".encode('utf-8') in registration_tab.get_attribute("aria-label").encode('utf-8'))

        # Check if the 'Congratulations!' message is visible after clicking the 'Next Step' button one last time
        congratulations_message = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name='congratulations']")))
        self.assertTrue("Congratulations!".encode('utf-8') in congratulations_message.text.encode('utf-8'))
        self.assertTrue(congratulations_message.get_attribute('class').encode('utf-8') == "message-box")

if __name__ == '__main__':
    unittest.main()