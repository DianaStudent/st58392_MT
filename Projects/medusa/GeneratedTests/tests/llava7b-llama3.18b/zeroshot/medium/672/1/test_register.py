import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Open the homepage
        self.driver.get('http://localhost:8000/dk')

        # Click the "Account" link
        account_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/dk/account"]')))
        account_link.click()

        # Click the "Join Us" button
        join_us_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        join_us_button.click()

        # Fill in all fields: first name, last name, email (generate it unique), password
        first_name_field = self.driver.find_element(By.NAME, 'first_name')
        last_name_field = self.driver.find_element(By.NAME, 'last_name')
        email_field = self.driver.find_element(By.NAME, 'email')
        password_field = self.driver.find_element(By.NAME, 'password')

        # Generate a unique email
        import uuid
        unique_email = str(uuid.uuid4()) + '@test.com'

        first_name_field.send_keys('user')
        last_name_field.send_keys('test')
        email_field.send_keys(unique_email)
        password_field.send_keys('testuser')

        # Submit the registration form
        join_us_button.click()

        # Verify registration success by checking presence of welcome message
        welcome_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="welcome-message"]')))
        self.assertIsNotNone(welcome_message.text)
        self.assertNotEqual('', welcome_message.text)

if __name__ == '__main__':
    unittest.main()