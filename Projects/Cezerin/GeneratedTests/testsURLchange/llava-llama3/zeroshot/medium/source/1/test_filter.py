import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import KeyAction
from selenium.webdriver.common.keys import Keys

class TestCategoryAFilter(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()
self.driver.get("http://localhost:3000/category-a")

def tearDown(self):
self.driver.quit()

def test_filter_brand_a(self):
# Apply the  "Brand A" checkbox filter by clicking on the checkbox input.
checkbox_filter = self.wait_for_element_by_css_selector('label[for="brandA"]')
self.driver.execute_script("arguments[0].click(arguments[1]);", [checkbox_filter, Keys.RIGHT_CLICK])
time.sleep(2)
# Uncheck the  "Brand A" filter.
uncheck_filter = self.wait_for_element_by_css_selector('label[for="brandA"]')
self.driver.execute_script("arguments[0].click(arguments[1]);", [uncheck_filter, Keys.LEFT_CLICK])

def test_filter_price(self):
# Use the interactive price slider component to change price filtering.
price_slider = self.wait_for_element_by_css_selector('input[name="priceSlider"]')

# Set a minimum price range (e.g., 100).
min_price = self.wait_for_element_by_css_selector('label[for="minPriceInput"]')
self.driver.execute_script("arguments[0].click(arguments[1]);", [min_price, Keys.LEFT_ARROW])

# Set a maximum price range (e.g., 200).
max_price = self.wait_for_element_by_css_selector('label[for="maxPriceInput"]')
self.driver.execute_script("arguments[0].click(arguments[1]);", [max_price, Keys.RIGHT_ARROW])

def test_filter_count(self):
# Verify that the number of displayed product cards changes (e.g., 2 → 1).
original_product_cards = self.wait_for_element_by_css_selector('div[data-product-count]')
product_cards = self.wait_for_element_by_css_selector('div[data-product-count]')

self.assertEqual(original_product_cards, product_cards)

# Uncheck the  "Brand A" filter.
uncheck_filter = self.wait_for_element_by_css_selector('label[for="brandA"]')
self.driver.execute_script("arguments[0].click(arguments[1]);", [uncheck_filter, Keys.LEFT_CLICK])

# Verify that the original number of product cards is restored (e.g., 1 → 2).
original_product_cards = self.wait_for_element_by_css_selector('div[data-product-count]')
product_cards = self.wait_for_element_by_css_selector('div[data-product-count]')

self.assertEqual(original_product_cards, product_cards)

if __name__ == '__main__':
unittest.main()