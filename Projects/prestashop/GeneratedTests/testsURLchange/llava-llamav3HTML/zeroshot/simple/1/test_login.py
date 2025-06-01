import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class PasswordLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_password_login(self):
        driver = self.driver
        base_url = 'http://localhost:8080/en/'

        # Go to the login page
        driver.get(f'{base_url}/login')

        # Locate the email input field by its label attribute
        email_label = driver.find_element_by_label('Email')
        email_input = email_label.find_element_by_xpath('*::input')

        # Locate the password input field by its label attribute
        password_label = driver.find_element_by_label('Password')
        password_input = password_label.find_element_by_xpath('*::input')

        # Type the email and password inputs with the given credentials
        email_input.send_keys('test@user.com')
        password_input.send_keys('test@user1')

        # Wait for 20 seconds before clicking on the login button
        login_button = driver.find_element_by_name('login-button')
        WebDriverWait(driver, 20).until(login_button.clickable)

        # Confirm success by checking that the text "Sign out" appear
        sign_out_text = driver.find_element_by_text('Sign out')
        self.assertTrue(sign_out_text.is_displayed())

if __name__ == '__main__':
    unittest.main()