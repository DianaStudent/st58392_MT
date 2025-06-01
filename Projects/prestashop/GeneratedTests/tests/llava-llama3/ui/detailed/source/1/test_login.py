import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestLoginPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_page_loaded(self):
self.assertEqual(self.driver.title, 'Clothes')

def test_main_components(self):
header = self.driver.find_element_by_xpath('html_data:xpath_header')
footer = self.driver.find_element_by_xpath('html_data:xpath_footer')

self.assertIsNotNone(header)
self.assertIsNotNone(footer)

form_fields = [self.driver.find_element_by_name('email'),
self.driver.find_element_by_name('password')]

for field in form_fields:
self.assertIsNotNone(field)
self.assertTrue(field.is_displayed())

def test_button_and_link(self):
create_account = self.driver.find_element_by_xpath('html_data:xpath_create_account')
login = self.driver.find_element_by_xpath('html_data:xpath_login')

self.assertIsNotNone(create_account)
self.assertIsNotNone(login)

def test_search_bar(self):
searchbar = self.driver.find_element_by_css_selector('input[name="q"]')

self.assertIsNotNone(searchbar)

if any([required_element not in html_data for required_element in ['header', 'footer', 'form_fields', 'create_account', 'login', 'searchbar']]):
self.fail("Required UI element missing")

def test_form_interaction(self):
email = self.driver.find_element_by_name('email')
password = self.driver.find_element_by_name('password')

email.send_keys('test@email.com')
password.send_keys('1234567890')

create_account_button = self.driver.find_element_by_name('register')

self.assertTrue(create_account_button.is_displayed())
create_account_button.click()

login_button = self.driver.find_element_by_name('login')

self.assertTrue(loginbutton.is_displayed())
loginbutton.click()

if any([loginbutton, create_accountbutton not in html_data]):
self.fail("Button with label 'login' or 'register' missing")

if any([required_element not in html_data for required_element in ['header', 'footer', 'form_fields', 'create_account', 'login', 'searchbar']]):
self.fail("Required UI element missing")

if any([email.get_attribute('value') != 'test@email.com',
password.get_attribute('value') != '1234567890']):
self.fail("Incorrect values for 'email' and 'password'")

def test_ui_reaction(self):
self.assertTrue(email.is_displayed())
self.assertTrue(password.is_displayed())

def test_required_elements(self):
if any([required_element not in html_data for required_element in ['header', 'footer', 'form_fields', 'create_account', 'login', 'searchbar']]):
self.fail("Required UI element missing")