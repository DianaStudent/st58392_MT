import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class TestAddToCart(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

# The provided HTML data
html_data = """
&lt;/tbody&gt;&lt;/table&gt;&ltp;div class=&q" + "unique"&gt;&ltp;div class=product"&gt;&ltp;"&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/d iv&gt;&ltp;/div&gt;&ltp;/div&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/div&gt;&ltp;/table&gt;&lt;/tbody&gt;&ltp;div class=&q" + "unique"&gt;&ltp;div class=product"&gt;&ltp;"&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/d iv&gt;&ltp;/div&gt;&ltp;/div&gt;&ltp;/table&gt;&lt;/tbody&gt;&ltp;/table&gt;&ltp;/tbody&gt;&ltp;/div&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&lt;/table&gt;&ltp;div class=&q" + "unique"&gt;&ltp;div class=product"&gt;&ltp;"&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/d iv&gt;&ltp;/div&gt;&ltp;/div&gt;&ltp;/table&gt;&ltp;/tbody&gt;&lt;/table&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&lt;/table&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&ltp;/table&gt;&ltp;/tbody&gt;&ltp;/div&gt;&ltp;/thead&gt;&ltp;/table&gt;&ltp;/tbody&gt;&ltp;/div&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&lt;/table&gt;&ltp;/tbody&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&lt;/table&gt;&ltp;/tbody&gt;&ltp;/div&gt;&ltp;"&g t;&ltp;/div&gt;&ltp;/tbody&gt;&ltp;/table&gt;&ltp;/thead&gt;&lt;/table&gt;&ltp;/tbody&gt;&ltp;/div&gt;&ltp/"&gt;
&lt/p;script&gt;&ltp;/body&gt;&ltp;/html&gt;

def tearDown(self):
self.driver.quit()

# The test cases
test_add_to_cart = [
{"product": "Category A"},
{"product": "Category B"},
{"product": "Category C"}
]
test_cases = len(test_add_to_cart)

def test_add_to_cart(self, index):
# Get the product to add from the provided test case
product_name = test_add_to_cart[index]["product"]
print(f"Test Case: {index} - Product Name: {product_name}")

# Find the product and click on it
product_element = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH, f"//*[contains(text(), '{product_name}')]}"))
ActionChains(self.driver).move_to_element(product_element).perform()

# Click the add to cart button
add_cart_button = self.driver.find_element_by_class_name("cart-button")
ActionChains(self.driver).move_to_element(add_cart_button).perform()

# Verify that the shopping bag is open and contains a product
shopping_bag_icon = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH, "//*[contains(text(), 'Shopping Bag')]")))
product_name = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
f"//*[contains(text(), '{product_name}')]}")))
ActionChains(self.driver).move_to_element(product_name).perform()

# Check the presence of 'Go to Checkout' button
self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'GO TO CHECKOUT')]"))))

if __name__ == "__main__":
unittest.main()