from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

class TestMaxPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_max_page(self):
# Open the page.
self.driver.get('http://max/')
# Confirm the presence of key interface elements: navigation links, inputs, buttons, banners.
self.assertElementPresence('html_data')
# Interact with one or two elements
# e.g., click a button and check that the UI updates visually.
input_username = self.driver.find_element_by_name('username')
input_password = self.driver.find_element_by_name('password')
button_login = self.driver.find_element_by_id('login')
button_login.click()
self.wait_for_element_appear('html_data')

def wait_for_element_appear(self, element_name):
try:
while True:
if self.driver.page_source().find(element_name).visible:
break
else:
time.sleep(0.5)
except KeyboardInterrupt as e:
e.printStackTrace()

if name == 'main':
TestMaxPage()
if name == 'register_page':
TestMaxPage()
if name == 'search_page':
TestMaxPage()
if name == 'login_page':
TestMaxPage()
if name == 'max_test':
TestMaxPage()
if name == 'unittest':
unittest.main()