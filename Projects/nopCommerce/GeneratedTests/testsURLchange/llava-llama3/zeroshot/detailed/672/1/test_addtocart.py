import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestIropCommerce(unittest.TestCase):
def setUp(self):
webdriver = webdriver.Chrome()
self.driver = webdriver

def tearDown(self):
self.driver.quit()

def test_search_and_add_to_cart(self):
# Step 1: Navigate to the homepage.
self.driver.get('http://max/')

# Step 2: Click on "Search" from the main menu.
search_menu = self.driver.find_element_by_css_selector('header > a[role="button"]')
self.driver.execute_script('arguments[0].click();', search_menu)

# Step 3: Type the search term "book" into the search field.
search_box = self.driver.find_element_by_css_selector('input[type="text"]')
self.driver.execute_script('arguments[0].value = "{}";'.format('book'))

# Step 4: Submit the search. # We don't have a submit button on this page, so we'll use the enter key to simulate submitting.

search_box.send_keys(Keys.RETURN)

# Step 5: Wait for the product grid to load.
product_grid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(('div', 'fls-c')))

# Step 6: Locate the first product result and click the "Add to cart" button.

first_product = WebDriverWait(product_grid, 20).until(
EC.element_to_be_clickable(
( By.XPATH, 'button[contains(text()="Add to Cart")]')))
self.driver.execute_script('arguments[0].click();', first_product)

# Step 7: Wait for the notification bar to appear "The product has been added to your shopping cart".
notification_bar = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located(('div', 'f3v-2')))
self.assertEqual(notification_bar.text, 'Product successfully added to cart')

# Step 8: From the notification, click the "shopping cart" link.
cart_link = self.driver.find_element_by_css_selector('a[role="button"][title="View cart"]')
self.driver.execute_script('arguments[0].click();', cart_link)

# Step 9: On the cart page, verify that the expected product is present.
cart_page_product = WebDriverWait(self.driver, 20).until(
EC.element_to_be_clickable((By.XPATH, 'div[contains(text()="First Book")]')))
self.assertTrue(cart_page_product.text().strip() == 'First Book')

if __name__ == '__main__':
unittest.main()