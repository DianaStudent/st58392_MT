import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_login(self):
        # Click the account icon
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#account-menu > a'))).click()
        except TimeoutException:
            self.fail('Timed out waiting for account menu item to be clickable')
        
        # Click the "Login" link
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()
        except TimeoutException:
            self.fail('Timed out waiting for login link to be clickable')

        # Enter email and password
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys('test2@user.com')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys('test11')
        except TimeoutException:
            self.fail('Timed out waiting for email and password fields to be present')

        # Click the login button
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login > .btn'))).click()
        except TimeoutException:
            self.fail('Timed out waiting for login button to be clickable')

        # Check that we've been redirected to the account page
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be('/my-account'))
        except TimeoutException:
            self.fail('Timed out waiting for URL to become /my-account')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()