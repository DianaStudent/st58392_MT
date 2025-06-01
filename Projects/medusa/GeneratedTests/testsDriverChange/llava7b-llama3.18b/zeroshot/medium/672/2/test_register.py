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
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Click the "Account" link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Account"))).click()
        
        # Click the "Join Us" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Join Us"))).click()

        # Fill in all fields: first name, last name, email (generate it unique), password.
        first_name_field = self.driver.find_element(By.NAME, 'first_name')
        first_name_field.send_keys('user')

        last_name_field = self.driver.find_element(By.NAME, 'last_name')
        last_name_field.send_keys('test')

        # Generate a new email
        import uuid
        email = f'user{uuid.uuid4()}@example.com'
        
        email_field = self.driver.find_element(By.NAME, 'email')
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys('testuser')

        # Submit the registration form.
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        register_button.click()

        # Verify registration success by checking presence of welcome message.
        welcome_message = self.driver.find_element(By.XPATH, "//h2").text
        self.assertEqual(welcome_message, 'Welcome')

if __name__ == '__main__':
    unittest.main()