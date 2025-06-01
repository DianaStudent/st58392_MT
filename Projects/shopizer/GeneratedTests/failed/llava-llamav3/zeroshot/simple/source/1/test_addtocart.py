from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestShoppingCart(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()
self.driver.get("http://localhost/")
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_add_to_cart(self):
# Hover over a product item to reveal the "Add to cart" button.
item_hovered = self.wait.until(EC.element_located_by_css_selector(".product-item:hover"))
item_button = item_hovered.find_element_by_xpath(".//button[@class='btn btn-primary']")
self.driver.execute_script("arguments[0].hover(parseInt(arguments[1]));", [item_hovered, item_button])

# Open the cart popup by clicking the cart icon.
cart_icon = self.wait.until(EC.element_located_by_css_selector(".shopping-cart-icon"))
self.driver.execute_script("arguments[0].click(parseInt(arguments[1]));", [cart_icon])

# Confirm success by checking that the popup contains at least one item.
item_in_popup = WebDriverWait(self.wait).until(
EC.text_to_be_present_in_elements(
["span[data-title]:contains('Olive Table')]", 20)))
self.assertTrue(item_in_popup)

def test_fill_cart(self):
# Use webdriver-manager to manage ChromeDriver.
driver = webdriver.Chrome()

# Open the cart popup by clicking the cart icon.
cart_icon = driver.find_element_by_css_selector(".shopping-cart-icon")
driver.execute_script("arguments[0].click(parseInt(arguments[1]));", [cart_icon])

# Confirm success by checking that the popup contains at least one item.
item_in_popup = WebDriverWait(driver).until(
EC.text_to_be_present_in_elements(
["span[data-title]:contains('Olive Table')]", 20)))
driver.quit()

if __name__ == '__main__':
unittest.main()