from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/')

    def test_login(self):
        # Click the account icon
        account_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-user']")))
        account_icon.click()

        # Click the "Login" link to open the login form
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()

        # Confirm success by checking that the browser is redirected to a page containing "/my-account" in the URL
        self.assertIn('/my-account', self.driver.current_url)

        # Fill out and submit the login form
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'password')))
        email_input.send_keys('test2@user.com')
        password_input.send_keys('test11**')

        # Submit the form
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()