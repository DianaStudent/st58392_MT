from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest from selenium import webdriver from selenium.webdriver.common.keys import Keys from time import sleep

class AddProductToCartTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_add_product_to_cart(self):
self.driver.get('http://localhost:8080/en/')

# Check if product is available in the catalog
product_name = self.find_element_by_label('name', 'The best is yet to come')
if product_name:
product_price = float(product_name.find_element_by_label('price').text)
self.assertEqual(product_price, 35.09)

# Add product to cart

success_message = self.find_element_by_label('blockcart-confirmation-title')
if not success_message:
self.fail("Error: No confirmation message found")

success_message_text = success_message.text.lower()
if "successfully added" in success_message_text:
else:
self.fail("Error: Product was not successfully added")

def find_element_by_label(self, label_name, value):
return self.driver.find_element_by_css_selector(f'{label_name}={value}')

if __name__ == '__main__':
unittest.main()