from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestEcommerceStore(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()
self.driver.get('http://localhost:8080/en/')

def tearDown(self):
self.driver.quit()

def test_main_ui_components(self):
headers, buttons, links, form_fields = self.find_main_ui_components()
assert headers
assert buttons
assert links
assert form_fields

def find_main_ui_components(self):
headers = self.wait_for_visible('header')
buttons = self.wait_for_visible('button')
links = self.wait_for_multiple('a', attribute='href')
form_fields = self.wait_for_multiple('input', attribute='name')
return headers, buttons, links, form_fields

def wait_for_visible(self, element_type):
return WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_tag_name(element_type))

def find_password_and_username_field(self):
username_field, password_field = self.wait_for_multiple('input', attribute='name')
return username_field, password_field

def test_login_feature(self):
username, password = self.wait_for_password_and_username()
self.driver.get('http://localhost:8080/en/login')

# check login form fields are visible
username_field, password_field = self.find_password_and_username_field()

# set values for username and password
username_field.send_keys(username)
password_field.send_keys(password)

# click on the 'submit' button
submit_button = self.wait_for_visible('button', attribute='type')
submit_button.click()

def wait_for_password_and_username(self):
return self.wait_for_multiple('input', attribute='name')

if \_\_name\_\_ == '\_\_main\_\_':
unittest.main()
```