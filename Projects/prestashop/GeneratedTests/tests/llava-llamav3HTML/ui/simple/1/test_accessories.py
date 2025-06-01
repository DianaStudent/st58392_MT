import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestSeleniumTest(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.base_url = 'http://localhost:8080/en/'
        self.clothes_url = 'http://localhost:8080/en/3-clothes'
        self.accessories_url = 'http://localhost:8080/en/6-accessories'
        self.art_url = 'http://localhost:8080/en/9-art'
        self.login_url = 'http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art'
        self.register_url = 'http://localhost:8080/en/registration'

    def tearDown(self):
        self.driver.quit()

    def test_selenium_test(self):
        # Check that the main UI components are present
        Assert.assertTrue(self.driver.find_element_by_tag_name('h1'))

        # Test clothes category
        self.driver.get(self.clothes_url)
        Assert.assertTrue(self.driver.find_element_by_text('Clothes'))

        # Test accessories category
        self.driver.get(self.accessories_url)
        Assert.assertTrue(self.driver.find_element_by_text('Accessories'))

        # Test art category
        self.driver.get(self.art_url)
        Assert.assertTrue(self.driver.find_element_by_text('Art'))

        # Log in
        self.driver.get(self.login_url)
        Assert.assertTrue(self.driver.find_element_by_name('email'))
        email = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('password')
        email.send_keys('test@example.com')
        password.send_keys('test_password')

        # Test registration
        self.driver.get(self.register_url)
        Assert.assertTrue(self.driver.find_element_by_name('name'))