from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from html_ data import *

def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

class EcoCommerceTest(unittest.TestCase):

def test_eco_commerce(self):
try:
# Test 1: Open page
driver.get('http://max/')

# Test 2: Confirm key interface elements
self.assertTrue(find_element_by_css_selector('header'))
self.assertTrue(find_element_by_css_selector('.main-nav li'))
self.assertTrue(find_element_by_css_selector('.search-button'))

# Test 3: Interact with one or two elements
element = find_element_by_css_selector('.search-button')
element.click()

# Verify that interactive elements do not cause errors in the UI
assert(element.get_attribute('data-bid') != '')

except:
self.fail('An error occurred during test execution')

if name == 'main':
unittest.main()