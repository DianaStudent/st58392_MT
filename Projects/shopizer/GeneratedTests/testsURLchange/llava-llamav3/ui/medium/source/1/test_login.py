from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class TestLoginPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_login_page(self):
url = 'http://localhost/login'
self.driver.get(url)

self.assertTrue(self.driver.page_source.find('button', value='Remember me'))
self.assertTrue(self.driver.page_source.find('a', href='/register'))

input_email = self.driver.page_source.find('input', name='email')
input_password = self.driver.page_source.find('input', name='password')

social_login_options = [self.driver.page_source.find('label', for_='facebook'), self.driver.page_source.find('label', for_='twitter')]

self.assertTrue(social_login_options)

for option in social_login_options:
social_login_options_dict = {}
option.get_attribute('id')
for id in social_login_options_dict.keys():
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))

# Test the login button
button_login = self.driver.page_source.find('button', value='Login')
ActionChains(self.driver).move_to_element(button_login).perform()

# Test the remember me checkbox
self.assertTrue(self.driver.page_source.find('label', for_='remember'))

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the facebook and twitter login options
for option in social_login_options:
social_login_options_dict[id].click()
self.assertTrue(self.driver.page_source.find('label', for_='facebook')) if id == 'facebook':
fb_link = self.driver.page_source.find('a', href='https://www.facebook.com/login')
fb_link.click()

self.assertTrue(self.driver.page_source.find('label', for_='twitter')) if id == 'twitter':
tw_link = self.driver.page_source.find('a', href='https://twitter.com/login')
tw_link.click()

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the forgot password link
forgot_password_link = self.driver.page_source.find('a', href='/register')

if self.driver.page_source.find('label', for_='remember'):
self.assertTrue(self.driver.page_source.find('checkbox', value='Remember me'))

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the social login buttons
for option in social_login_options:
social_login_options_dict[id].click()
self.assertTrue(self.driver.page_source.find('label', for_='login')) if id == 'facebook':
fb_link = self.driver.page_source.find('a', href='https://www.facebook.com/login')
fb_link.click()

self.assertTrue(self.driver.page_source.find('label', for_='login')) if id == 'twitter':
tw_link = self.driver.page_source.find('a', href='https://twitter.com/login')
tw_link.click()

def test_login_failure(self):
url = 'http://localhost/login'
self.driver.get(url)

input_email = self.driver.page_source.find('input', name='email')
input_password = self.driver.page_source.find('input', name='password')

# Test the login button
button_login = self.driver.page_source.find('button', value='Login')
ActionChains(self.driver).move_to_element(button_login).perform()

self.assertFalse(input_email.get_attribute('value'))
self.assertFalse(input_password.get_attribute('value'))

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the facebook and twitter login options
for option in social_login_options:
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
self.assertFalse(social_login_options_dict[id].get_attribute('href'))

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the forgot password link
forgot_password_link = self.driver.page_source.find('a', href='/register')

if self.driver.page_source.find('label', for_='remember'):
self.assertFalse(self.driver.page_source.find('checkbox', value='Remember me'))

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the social login buttons
for option in social_login_options:
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
self.assertFalse(social_login_options_dict[id].get_attribute('href'))

def test_register_page(self):
url = 'http://localhost/register'
self.driver.get(url)

input_email = self.driver.page_source.find('input', name='email')
input_password = self.driver.page_source.find('input', name='password')

social_login_options = [self.driver.page_source.find('label', for_='facebook'), self.driver.page_source.find('label', for_='twitter')]

self.assertTrue(social_login_options)

for option in social_login_options:
social_login_options_dict = {}
option.get_attribute('id')
for id in social_login_options_dict.keys():
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))

# Test the register button
button_register = self.driver.page_source.find('button', value='Register')
ActionChains(self.driver).move_to_element(button_register).perform()

# Test the facebook and twitter login options
for option in social_login_options:
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
self.assertTrue(self.driver.page_source.find('label', for_='facebook')) if id == 'facebook':
fb_link = self.driver.page_source.find('a', href='https://www.facebook.com/login')
fb_link.click()

self.assertTrue(self.driver.page_source.find('label', for_='twitter')) if id == 'twitter':
tw_link = self.driver.page_source.find('a', href='https://twitter.com/login')
tw_link.click()

if self.driver.page_source.find('input', name='email'):
email_input = input_email.get_attribute('value')

if self.driver.page_source.find('input', name='password'):
password_input = input_password.get_attribute('value')

# Test the social login buttons
for option in social_login_options:
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
self.assertTrue(self.driver.page_source.find('label', for_='login')) if id == 'facebook':
fb_link = self.driver.page_source.find('a', href='https://www.facebook.com/login')
fb_link.click()

self.assertTrue(self.driver.page_source.find('label', for_='login')) if id == 'twitter':
tw_link = self.driver.page_source.find('a', href='https://twitter.com/login')
tw_link.click()

def test_tables_page(self):
url = 'http://localhost/category/tables'
self.driver.get(url)

table_header = self.driver.page_source.find('thead')

if table_header:
table_header_text = []
for th in table_header:

# Test the table header text
self.assertEqual(table_header_text, ['Category', 'Tables'])

# Test the table body content
table_body = self.driver.page_source.find('tbody')

if table_body:
rows = []
for tr in table_body:

# Test the table row content
self.assertTrue(tr.get_attribute('data-original-title'))
self.assertTrue(row_text == 'Table 1')

# Test the next and previous buttons
next_button = self.driver.page_source.find('button', value='Next')
prev_button = self.driver.page_source.find('button', value='Previous')

if self.driver.page_source.find('label', for_='tables'):
next_button.click()
self.assertTrue(next_button.get_attribute('data-original-title'))
prevbutton = self.driver.page_source.find('button', value='Previous')

if self.driver.page_source.find('label', for_='tables'):
prevbutton.click()
self.assertTrue(prevbutton.get_attribute('data-original-title'))

# Test the social login options
social_login_options_dict = {}
self.driver.page_source.find('label', for_='social-login')
for option in social_login_options_dict.keys():
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
if social_login_options_dict['fb']:
fb_link = self.driver.page_source.find('a', href='https://www.facebook.com/login')

# Test the social login buttons
for option in social_login_options:
social_login_options_dict[id] = self.driver.page_source.find('a', id=hash(id))
self.assertTrue(self.driver.page_source.find('label', for_='login')) if id == 'fb':
fb_link.click()

if social_login_options_dict['tw']:
tw_link = self.driver.page_source.find('a', href='https://twitter.com/login')

# Test the forgot password link
forgot_password_link = self.driver.page_source.find('a', href='/register')

if self.driver.page_source.find('label', for_='tables'):
self.assertTrue(self.driver.page_source.find('h1', text='Tables'))

if self.driver.page_source.find('label', for_='social-login'):
self.assertTrue(self.driver.page_source.find('button', value='Next'))
self.assertTrue(self.driver.page_source.find('button', value='Previous'))