from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Key

class TestSimplerOrderCompletion(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome("chromedriver.exe")
self.driver = driver

def tearDown(self):
self.driver.quit()

def test_simpler_order_completion(self):
# Add product to cart
shoppingbag = WebDriverWait(self.driver, 20).until_element_located((By.XPATH,
"//span[contains(text(), 'Shopping Bag')]"))
self.assertTrue(shoppingbag.is_displayed())

# Wait for checkout button
checkbutton = WebDriverWait(self.driver, 20).until_element_located((By.XPATH, "//a[contains(text(), 'Go to Checkout')]"))
self.assertTrue(checkbutton.is_displayed())

# Fill required checkout fields
email = self.driver.find_element_by_name("email")
phone = self.driver.find_element_by_name("phone")
shipping_address = self.driver.find_element_by_name("shipping-address")
shipping_method = Select(self.driver.find_element_by_name("shipping-method"))
payment_method = Select(self.driver.find_element_by_name("payment-method"))

# Place order
order_button = self.driver.find_element_by_css_selector(".btn-primary")
self.assertTrue(order_button.is_displayed())
order_button.click()

# Confirm successful order completion
success_message = WebDriverWait(self.driver, 20).until_element_located((By.XPATH,
"//div[contains(text(), 'Thanks for your order!')]"))
self.assertTrue(success_message.is_displayed())

def test_simpler_order_completion(self):
# Add product to cart
shoppingbag = WebDriverWait(self.driver, 20).until_element_located((By.XPATH,
"//span[contains(text(), 'Shopping Bag')]"))
self.assertTrue(shoppingbag.is_displayed())

# Wait for checkout button
checkbutton = WebDriverWait(self.driver, 20).until_element_located((By.XPATH, "//a[contains(text(), 'Go to Checkout')}