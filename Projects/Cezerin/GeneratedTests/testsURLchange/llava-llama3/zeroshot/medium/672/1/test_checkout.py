import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities.html_data import html_ data

class CheckoutTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_checkout_process(self):
url = "http://localhost:3000/"
html_data.load_html("html_data/checkout_test.html")
product_category = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH,
html_data.product_categories[0]))
)
product_category.click()
product = WebDriverWait(product_category,
20).until(EC.presence_of_element_located((By.XPATH,
html_data.product_card[0])))
product.click()
add_to_cart_button = WebDriverWait(product,
20).until(EC.presence_of_element_located((By.XPATH,
html_data.add_to_cart_button)))
add_to_cart_button.click()
cart_icon = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH,
html_data.cart_icon))
)
cart_icon.click()

if self.assertEqual(len(self.driver.current_url.split("/")), 5):
self.fail("Failed to go to checkout")

next_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.next_button)))
nextbutton_clickable = WebDriverWait(nextbutton, 20).until(
EC.element_to_be_clickable(By.XPATH,
html_data.next_button)
)

while nextbutton_clickable.is_clickable():
nextbutton_clickable.click()

place_order_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.place_order_button)))
place_order_button_clickable = WebDriverWait(place_order_button, 20).until(
EC.element_to_be_clickable(By.XPATH,
html_data.place_order_button)
)

while place_order_button_clickable.is_clickable():
place_order_button_clickable.click()

success_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.success_message)))
self.assertEqual(success_message.get_attribute("textContent"),
"Thanks for your order!")

if self.assertEqual(len(self.driver.current_url.split("/")), 6):
self.fail("Failed to go to checkout")

def test_order_confirmation(self):
url = "http://localhost:3000/checkout"
html_data.load_html("html_data/checkout_test.html")
order_receipt_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_receipt_button)))
order_receipt_button_clickable = WebDriverWait(order_receipt_button, 20).until(
EC.element_to_be_clickable(By.XPATH,
html_data.order_receipt_button)
)

while order_receipt_button_clickable.is_clickable():
order_receipt_button_clickable.click()

order_receipt_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_receipt_message)))
self.assertEqual(orderreceipt_message.get_attribute("textContent"),
"Thanks for your order!")

if self.assertEqual(len(self.driver.current_url.split("/")), 7):
self.fail("Failed to go to checkout")

def test_order_completion(self):
url = "http://localhost:3000/checkout"
html_data.load_html("html_data/checkout_test.html")
order_completion_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_completion_button)))
order_completion_button_clickable = WebDriverWait(order_completion_button, 20).until(
EC.element_to_be_clickable(By.XPATH,
html_data.order_completion_button)
)

while order_completion_button_clickable.is_clickable():
order_completion_button_clickable.click()

order_completion_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_completion_message)))
self.assertEqual(ordercompletion_message.get_attribute("textContent"),
"Thanks for your order!")

if self.assertEqual(len(self.driver.current_url.split("/")), 8):
self.fail("Failed to go to checkout")

def test_order_confirmation_and_completion(self):
url = "http://localhost:3000/checkout"
html_data.load_html("html_data/checkout_test.html")
order_confirmation_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_confirmation_button)))
order_confirmation_button_clickable = WebDriverWait(order_confirmation_button, 20).until(
EC.element_to_be_clickable(By.XPATH,
html_data.order_confirmation_button)
)

while order_confirmation_button_clickable.is_clickable():
order_confirmation_button_clickable.click()

order_confirmation_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_confirmation_message)))
self.assertEqual(orderconfirmation_message.get_attribute("textContent"),
"Thanks for your order!")

if self.assertEqual(len(self.driver.current_url.split("/")), 9):
self.fail("Failed to go to checkout")

def test_order_completion_and_order_confirmation(self):
url = "http://localhost:3000/checkout"
html_data.load_html("html_data/checkout_test.html")
order_completion_and_order_confirmation_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
html_data.order_completion_and_order_confirmation_button)))
order_completion_and_order_confirmation_clickable = WebDriverWait(order_completion_and_order_configuration
```