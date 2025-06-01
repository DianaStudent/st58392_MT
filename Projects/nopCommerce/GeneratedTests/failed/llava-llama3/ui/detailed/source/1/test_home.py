from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestYCommerceWebpage(unittest.TestCase):
def setUp(self):
# Set up the chromedriver path
driver_manager = ChromeDriverManager()

# Create a new instance of the WebDriver using the ChromeDriverManager and ChromeOptions
options = Options()
options.binary_location = driver_manager-binary_path
self.driver = webdriver.Chrome(options=options)

def tearDown(self):
# Close the WebDriver after each test

self.driver.quit()

def test_load_page(self):
# Load the main page
self.driver.get('http://max/')

# Verify that structural elements (e.g., header, footer, navigation) are visible
assert self.driver.find_element_by_tag_name('header')
assert self.driver.find_element_by_tag_name('footer')
assert self.driver.find_element_by_tag_name('nav')

def test_login_page(self):
# Load the login page
self.driver.get('http://max/login?returnUrl=%2F')

# Verify that input fields, buttons, labels, and sections are visible and interactable
login_username = self.driver.find_element_by_id('username')
assert self.driver.find_element_by_id('password')
assert self.driver.find_element_by_name('remember')
assert self.driver.find_element_by_id('loginButton')

def test_register_page(self):
# Load the register page
self.driver.get('http://max/register?returnUrl=%2F')

# Verify that input fields, buttons, labels, and sections are visible and interactable
register_username = self.driver.find_element_by_id('username')
assert self.driver.find_element_by_id('password')
assert self.driver.find_element_by_name('agree')
assert self.driver.find_element_by_id('registerButton')

def test_search_page(self):
# Load the search page
self.driver.get('http://max/search')

# Verify that input fields, buttons, labels, and sections are visible and interactable
search_input = self.driver.find_element_by_name('q')
assert self.driver.find_element_by_name('submit')

if __name__ == '__main__':
unittest.main()