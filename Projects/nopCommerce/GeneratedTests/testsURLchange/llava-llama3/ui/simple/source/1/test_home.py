import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class MaxTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_home_page(self):
url = 'http://max/'
self.assertTrue('Your Commerce' in self.driver.title())

def test_login_page(self):
url = 'http://max/login?returnUrl=%2F'
self.assertTrue('Login' in self.driver.title())
self.assertTrue('#login-email' in self.driver.page_source)
self.assertTrue('#login-password' in self.driver.page_source)

def test_register_page(self):
url = 'http://max/register?returnUrl=%2F'
self.assertTrue('Register' in self.driver.title())
self.assertTrue('#register-email' in self.driver.page_source)
self.assertTrue('#register-password' in self.driver.page_source)

def test_search_page(self):
url = 'http://max/search'
self.assertTrue('Search' in self.driver.title())
self.assertTrue('#search-input' in self.driver.page_source)

if __name__ == '__main__':
unittest.main()