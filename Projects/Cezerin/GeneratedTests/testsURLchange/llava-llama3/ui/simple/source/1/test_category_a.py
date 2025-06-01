from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

    def tearDown(self):
        self.driver.quit()

    def test_register_form(self):
        self.driver.get('http://localhost:3000')
        time.sleep(2)
        registration_form = self.wait_for_element_by_id('registration-form')
        
        sign_up_button = self.find_element_by_name('Sign up')
        forgot_password_button = self.find_element_by_name('Forgot password?')

        first_name_field = self.find_element_by_name('First name')
        last_name_field = self.find_element_by_name('Last name')

        category_a_link = self.wait_for_element_by_tagname('a', text='Category A')
        category_a_1_link = self.wait_for_element_by_tagname('a', text='Category A-1')

    def wait_for_element_by_id(self, id):
        return WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(by=Keys.ID, value=id))

if __name__ == '__main__':
    unittest.main()