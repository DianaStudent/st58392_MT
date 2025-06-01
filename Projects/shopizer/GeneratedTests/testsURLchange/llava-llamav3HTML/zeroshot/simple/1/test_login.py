import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get('http://localhost/')

        # wait for the user name field to appear and fill it with the email provided
        user_name_field = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_name('userName'))
        user_name_field.send_keys("test2@user.com")
        
        # wait for the password field to appear and fill it with the password provided
        pass_word_field = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_name('password'))
        pass_word_field.send_keys("test**11")

        # click the login button
        login_button = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_name('loginBtn'))
        login_button.click()

        # wait for the redirect to the account page and confirm success by checking that the browser is redirected to a page containing "/my-account" in the URL
        my_account_url = driver.current_url
        self.assertTrue("/my-account" in my_account_url)

if __name__ == '__main__':
    unittest.main()