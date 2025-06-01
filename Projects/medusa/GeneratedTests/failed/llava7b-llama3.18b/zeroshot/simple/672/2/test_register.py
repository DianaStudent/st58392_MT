from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestRegistrationSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_register_simple(self):
        # Get form elements
        name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "name")))
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))

        # Fill form
        name_field.send_keys("user")
        email_field.send_keys("testuser" + str(12345) + "@example.com") # generate unique email address
        password_field.send_keys("testuser")

        # Click next button
        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        next_button.click()

        # Check welcome message
        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='welcome-message']")))
        self.assertEqual(welcome_message.text, "Hello User")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()