import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to registration page
        account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'My account')))
        account_link.click()

        # Fill out registration form
        try:
            gender = wait.until(EC.presence_of_element_located((By.ID, 'gender-male')))
            gender.click()

            first_name = driver.find_element(By.ID, 'FirstName')
            first_name.send_keys('John')

            last_name = driver.find_element(By.ID, 'LastName')
            last_name.send_keys('Doe')

            email = driver.find_element(By.ID, 'Email')
            random_email = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '@example.com'
            email.send_keys(random_email)

            company = driver.find_element(By.ID, 'Company')
            company.send_keys('TestCompany')

            password = driver.find_element(By.ID, 'Password')
            password.send_keys('test11')

            confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
            confirm_password.send_keys('test11')

            register_button = driver.find_element(By.ID, 'register-button')
            register_button.click()

            # Verify registration success message
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))
            self.assertIn('Your registration completed', success_message.text)

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()