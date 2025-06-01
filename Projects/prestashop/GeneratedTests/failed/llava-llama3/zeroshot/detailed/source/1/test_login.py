from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.email = 'test@user.com'
        self.password = 'test@user1'

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Step 2 - Click the login link from top navigation
        self.login_link = self.driver.find_element_by_id('header-login-link')
        self.login_link.click()
        
        # Step 3 - Fill in email and password fields using test credentials provided
        self.email_field = WebDriverWait(self.driver, 20).until(
            presence_of_element_located((By.ID, 'email')))
        self.password_field = WebDriverWait(self.driver, 20).until(
            presence_of_element_located((By.ID, 'password')))
        
        # Step 4 - Click the submit button
        self.submit_button = WebDriverWait(self.driver, 20).until(
            element_to_be_clickable((By.ID, 'login-button')))
        self.submit_button.click()
        
        # Step 6 - Confirm that login was successful by checking that:
        #         The "Sign out" button is present in the top navigation
        #         The username (e.g. "test user") is also visible in the top navigation
        self.sign_out_button = WebDriverWait(self.driver, 20).until(
            element_to_be_clickable((By.ID, 'header-sign-out-link')))
        self.username_text = WebDriverWait(self.driver, 20).until(
            presence_of_element_located((By.ID, 'header-username-text')))

        # Step 7 - Check if all requirements are met
        self.assertEqual(self.sign_out_button, "Sign out")
        self.assertEqual(self.username_text, "test user")

if __name__ == '__main__':
    unittest.main()