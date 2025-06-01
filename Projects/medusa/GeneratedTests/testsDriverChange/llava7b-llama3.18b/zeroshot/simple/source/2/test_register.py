import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegisterSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_register_simple(self):
        # Register button
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/register']")))
        register_button.click()

        # First Name and Last Name fields
        first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "first_name")))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "last_name")))

        # Fill First Name and Last Name fields
        first_name_field.send_keys("user")
        last_name_field.send_keys("test")

        # Next button
        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        next_button.click()

        # Email and Password fields
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))

        # Fill Email and Password fields
        email_field.send_keys("testuser@example.com")
        password_field.send_keys("testuser")

        # Submit button
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Welcome message
        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome!']")))

    def test_error_handling(self):
        # Register button
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/register']")))
        register_button.click()

        # Submit button with empty fields
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Error message
        error_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='error-message']")))

if __name__ == '__main__':
    unittest.main()