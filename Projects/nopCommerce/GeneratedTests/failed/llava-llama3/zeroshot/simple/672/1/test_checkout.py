from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.text import Text
from selenium.webdriver.support.button import Button
from selenium.webdriver.support.checkbox import Checkbox
from selenium.webdriver.support.filefield import FileField
from selenium.webdriver.support.color import Color

class TestGuestOrderCompletion(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.driver.maximize_window()

def tearDown(self):
self.driver.quit()

def test_guest_order_completion(self):
try:
# Search for a product (e.g. "book")
product_search = WebDriverWait(self.driver, 20).until(
Text("input[name='search']"),
"Product search field not found.")
product_search.send_keys("book")
product_search.send_keys(Keys.RETURN)
# Add the product to cart
shopping_cart_button = WebDriverWait(self.driver, 20).until(
Button("span", "Shopping Cart button not found."),
"A 'Shopping Cart' button is missing.")
shopping_cart_button.click()

# Click on the shopping cart button
shopping_cart_popup = WebDriverWait(self.driver, 20).until(
Text("div[role='dialog']"),
"Shopping cart popup not found.")
popup_title = WebDriverWait(self.driver, 20).until(
Text("h1"),
"A 'Shopping cart' title is missing.")

# Use the "Checkout as Guest" option
guest_checkout_button = WebDriverWait(popup_title, 20).until(
Button("button", "Guest checkout button not found."),
"A 'Guest checkout' button is missing.")
guest_checkout_button.click()

# Confirm order completion by checking for an order completion message
order_completion_message = WebDriverWait(self.driver, 20).until(
Text("div[role='dialog']"),
"Order completion message not found.")
order_completion_message_text = order_completion_message.text

if order_completion_message_text == "Order completed successfully":
unittest.assertTrue(self.order_complet
```