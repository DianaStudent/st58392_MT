from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class TestAccessories(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome()

def tearDown(self):
pass

def test_accessories(self):
url = 'http://localhost:8080/en/6-accessories'
self.driver.get(url)
category_list = self.find_element('css','div.catalog-list')
assert category_list is not None
assert category_list.get_attribute('class') == 'ui-tabs-vertical ui-api'

for i in range(1, 7):
item = self.find_element('css','div.catalog-item:nth-child(%d)' % i)
assert item is not None
assert item.get_attribute('class') == 'ui-state-default ui-corner-rounded'
name = item.find_element_by_tag_name('a')
assert name.is_displayed()
cat_name = item.find_element_by_tag_name('span')
assert cat_name.is_displayed()
self.driver.execute_script("arguments[0].scrollIntoView();", name)
item_name = self.find_element('css','div.catalog-item:nth-child(%d) span' % i)
assert item_name.is_displayed()

def test_accessories_category(self):
url = 'http://localhost:8080/en/'
self.driver.get(url)

category_name = 'Accessories'
category_filter = self.find_element_by_id('idCategoryFilter')
assert category_filter is not None
assert category_filter.get_attribute('value') == category_name

for i in range(1, 7):
item_name = self.find_element('css','div.catalog-item:nth-child(%d) span' % i)
assert item_name.is_displayed()
self.driver.execute_script("arguments[0].scrollIntoView();", item_name)

def test_accessories_category_with_filter(self):
url = 'http://localhost:8080/en/'
self.driver.get(url)

category_name = 'Art'
category_filter = self.find_element_by_id('idCategoryFilter')
assert category_filter is not None
assert category_filter.get_attribute('value') == category_name

for i in range(1, 7):
item_name = self.find_element('css','div.catalog-item:nth-child(%d) span' % i)
assert item_name.is_displayed()
self.driver.execute_script("arguments[0].scrollIntoView();", item_name)

if __name__ == '__main__':
unittest.main()