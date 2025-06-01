from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.keys import Keys

# Set up WebDriver instance
driver = webdriver.Chrome("/path/to/chromedriver")

def setUp(self):
self.driver = driver

def tearDown(self):
self.driver.quit()

def test_order_process():
try:
# Add a product to the cart
cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cart_button))
cart_button.click()

# Wait for presence of "GO TO CHECKOUT" button using html_data
checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.checkout_button))

# Fill required checkout fields (e.g. email, phone, shipping address, Shipping, payment) using values visible in html_data
email_field = self.email_field
phone_field = self.phone_field
address_field = self.address_field
shipping_method_field = self.shipping_method_field
payment_method_field = self.payment_method_field

email = email_field.get_attribute("data-email")
phone = phone_field.get_attribute("data-phone")
address = address_field.get_attribute("data-address")
shipping_method = shipping_method_field.select_by_visible_text("Shipping")
payment_method = payment_method_field.select_by_visible_text("Payment")

# Place the order
order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.order_button))
order_button.click()

# Confirm that the final success page contains the text: "Thanks for your order!"
final_message = WebDriverWait(self.driver, 20).until(EC.text_to_be("Thanks for your order!"))
self.assertEqual(final_message, "Thanks for your order!")

except Exception as e:
print(f"Error occurred during test: {str(e)}")
if not self.email_field.is_displayed():
self.fail("Email field is missing.")
if not self.phone_field.is_displayed():
self.fail("Phone field is missing.")
if not self.address_field.is_displayed():
self.fail("Address field is missing.")
if not self.shipping_method_field.is_displayed():
self.fail("Shipping method field is missing.")
if not self.payment_method_field.is_displayed():
self.fail("Payment method field is missing.")

# Close the browser window
driver.quit()