from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.support.assertions import Assert

class TestRegistrationPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.driver.implicitly_wait(20, "visible")

def tearDown(self):
self.driver.quit()

def test_register_page(self):
try:
self.driver.get("http://max/register?returnUrl=%2F")
assert self.is_element_present_by_css_selector(".block.header", 'text')
assert self.is_element_present_by_css_selector(".block.block", 'text')
assert self.is_element_present_by_css_selector(".block.content", 'text')

# Fill the form
first_name = Select(self.driver.find_element_by_id('cboFirstName'))
last_name = self.driver.find_element_by_id('tbxLastName')
first_name.select_by_index(0)
last_name.send_keys("John")
first_name.select_by_index(1)

# Click on register now button
register_now_button = self.driver.find_element_by_css_selector('.block.button')
register_now_button.click()

assert self.is_element_present_by_css_selector(".block.header", 'text')
assert self.is_element_present_by_css_selector(".block.block", 'text')
assert self.is_element_present_by_css_selector(".block.content", 'text')

# Check the account has been registered
self.driver.get("http://max/login?returnUrl=%2F")
assert self.is_element_present_by_css_selector(".block.header", 'text')

except Exception as e:
self.fail(str(e))

if __name__ == '__main__':
unittest.main()