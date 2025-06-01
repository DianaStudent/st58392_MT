import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestAddToCart(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_add_to_cart(self):
# 1. Open the home page.
self.driver.get('http://localhost/')

# 2. Hover over a product item to reveal the "Add to cart" button.
product_item = self.driver.find_element_by_css_selector('.col-lg-4')
action_chains = ActionChains(self.driver)
action_chains.move_to_element(product_item)

# 3. Click the "Add to cart" button.
add_to_cart_button = self.driver.find_element_by_css_selector('.btn-primary')
add_to_cart_button.click()

# 4. Open the cart popup by clicking the cart icon.
cart_popup_icon = self.driver.find_element_by_css_selector('.icon-cart')
cart_popup_icon.click()

# Verify that at least one product is listed in the popup cart.
cart_items = self.driver.find_elements_by_css_selector('.item-list')
self.assertEqual(len(cart_items), at least 1)

def test_add_to_cart_fails(self):
# 1. Open the home page.
self.driver.get('http://localhost/')

# 2. Hover over a product item to reveal the "Add to cart" button.
product_item = self.driver.find_element_by_css_selector('.col-lg-4')
action_chains = ActionChains(self.driver)
action_chains.move_to_element(product_item)

# 3. Open the cart popup by clicking the cart icon.
cart_popup_icon = self.driver.find_element_by_css_selector('.icon-cart')
cart_popup_icon.click()

# Check that the popup cart has no items
cart_items = self.driver.find_elements_by_css_selector('.item-list')
self.assertEqual(len(cart_items), 0)

def test_add_to_cart_fails_empty_product(self):
# 1. Open the home page.
self.driver.get('http://localhost/')

# 2. Hover over a product item to reveal the "Add to cart" button.
product_item = self.driver.find_element_by_css_selector('.col-lg-4')
action_chains = ActionChains(self.driver)
action_chains.move_to_element(product_item)

# 3. Click the "Add to cart" button.
add_to_cart_button = self.driver.find_element_by_css_selector('.btn-primary')
add_to_cart_button.click()

# Check that the popup cart has no items
cart_popup_icon = self.driver.find_element_by_css_selector('.icon-cart')
cart_popup_icon.click()
cart_items = self.driver.find_elements_by_css_selector('.item-list')
self.assertEqual(len(cart_items), 0)

if __name__ == '__main__':
unittest.main()