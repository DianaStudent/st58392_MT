from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from unittest import TestCase, setUp, tearDown
import html_data

class TestSearchPage(TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()
if not self.test_search():
raise self.failureException('Test case failed')

def test_search(self):
self.driver.get(html_data.search_page)
time.sleep(20)
assert self.driver.find_element_by_name('search')

def is_ui_present(key_interface_elements):
for element in key_interface_elements:
if not self.driver.find_element_by_name(element):
return False
return True

def is_ui_interactive(key_interface_elements):
for element in key_interface_elements:
if not self.driver.find_element_by_name(element):
return False
self.assertTrue(self.driver.find_element_by_name(element).is_enabled())
return True

if __name__ == '__main__':
unittest.main()
```