import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.action import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Alerts
from selenium.webdriver.common.interaction import InteractiveElements
from selenium.webdriver.common.contextual import ContextualElements
from selenium.webdriver.common.key import Keys
from webdriver_manager.chrome import ChromeDriverManager

class MaxEcommerceTest(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())
self.driver = driver

def tearDown(self):
self.driver.quit()

def test_homepage(self):
# Open the homepage
self.driver.get('http://max/')
assert self.find_element_by_css_selector('.nav-link')

def test_login_page(self):
# Open the login page
self.driver.get('http://max/login?returnUrl=%2F')
assert self.find_element_by_css_selector('#loginusername')

def test_register_page(self):
# Open the register page
self.driver.get('http://max/register?returnUrl=%2F')
assert self.find_element_by_css_selector('#registeremail')

def test_search_page(self):
# Open the search page
self.driver.get('http://max/search')
assert self.find_element_by_css_selector('#searchinput')

if __name__ == '__main__':
unittest.main()