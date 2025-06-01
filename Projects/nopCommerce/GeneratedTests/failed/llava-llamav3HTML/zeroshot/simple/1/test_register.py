from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://max/'

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Generate a unique email address
        email_address = "testuser" + str(int(time.time())) + "@example.com"
        
        # Navigate to the registration page
        self.driver.get(self.url)

        # Fill out all fields for registration
        gender_select = WebDriverWait(self.driver, 20).until(
            lambda x: Select(x.find_element_by_name("gender"))
        )
        gender_select.select_by_visible_text('Male')

        first_name_input = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("FirstName")
        )
        last_name_input = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("LastName")
        )
        password_input = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("Password")
        )
        confirm_password_input = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("ConfirmPassword")
        )

        first_name_input.send_keys('John')
        last_name_input.send_keys('Doe')
        password_input.send_keys('test11')
        confirm_password_input.send_keys('test11')

        # Submit the registration form
        register_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_id("register-button")
        )
        register_button.click()

        # Check if the message "Your registration completed" is shown after successful registration
        result_message = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector('div.result')
        )
        self.assertEqual(result_message.text, 'Your registration completed')

if __name__ == '__main__':
    unittest.main()