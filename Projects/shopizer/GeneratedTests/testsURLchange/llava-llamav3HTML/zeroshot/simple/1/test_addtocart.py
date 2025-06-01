import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import SelectElement
from selenium.webdriver.support.ui import WebDriverWait

class TestSeleniumTasks(unittest.TestCase):
def setUp(self):
# Use webdriver-manager to manage ChromeDriver
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_add_to_cart(self):
# Hover over a product item to reveal the "Add to cart" button.
product_item = self.driver.find_element_by_css_selector("table>tbody>tr>td>div.product-thumbnail")
ActionChains(self.driver).move_to_element(product_item)

# Click the "Add to cart" button
add_to_cart_button = self.driver.find_element_by_css_selector(".product-price-cart>button[aria-label='ADD TO CART']")
WebDriverWait(self.driver, 20).until(add_to_cart_button.is_clickable())
add_to_cart_button.click()

# Open the cart popup by clicking the cart icon.
cart_icon = self.driver.find_element_by_css_selector("span.cart-icon")
ActionChains(self.driver).move_to_element(cart_icon)

# Confirm success by checking that the popup contains at least one item.
WebDriverWait(self.driver, 20).until(lambda x: x.title_of_locator == 'Cart')
if "Grand Total" not in self.driver.page_source:
self.fail("No items added to cart")

def test_manager_chrome(self):
# Use webdriver-manager to manage ChromeDriver
self.driver = webdriver.Chrome()

# Test if ChromeDriver is successfully installed and running.
try:
assert(self.driver.title == "Manager")
except:
assert(False, "ChromeDriver not installed or not running.")
if __name__== '__main__':
unittest.main()