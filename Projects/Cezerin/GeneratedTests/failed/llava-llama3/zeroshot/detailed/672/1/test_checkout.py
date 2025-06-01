from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import assert_true

class CheckoutTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.driver.implicitly_wait(10, 'time')
self.url = 'http://localhost:3000/'

def tearDown(self):
self.driver.quit()

def test_checkout(self):
# Step 1: Open home page
self.driver.get(self.url)

# Step 2: Click on product category
category_button = self.wait_for_element_by_name('product-categories')
category_button.click()

# Step 3: Select the first product
first_product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/a')))
first_product.click()

# Step 4: Click the cart icon/button to open the shopping bag
cart_icon_button = self.wait_for_element_by_name('cart-button')
cart_icon_button.click()

# Step 5: Verify that the "GO TO CHECKOUT" button is present inside the cart
checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/button[@data-tip="View Cart"]')))
assert_true(checkoutbutton)

# Step 6: Click the "GO TO CHECKOUT" button
checkoutbutton.click()

# Step 7: Wait for the checkout form to appear
checkoutform = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[1]/form')))

# Step 8: Fill out the checkout form fields using the following credentials:
email_input = self.wait_for_element_by_name('email')
email_input.send_keys('mail@mail.com')

phone_input = self.wait_for_element_by_name('phone')
phone_input.send_keys(12345678)

state_input = self.wait_for_element_by_name('state')
state_input.select_by_value('Riga')

city_input = self.wait_for_element_by_name('city')
city_input.send_keys('Riga')

# Step 9: Select a shipping method and a payment method
shipping_method_select = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/select[@name="shipping-method"]')))
payment_method-select = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/select[@name="payment-method"]')))

# Step 10: Click the "Next" button
next_button = self.wait_for_element_by_name('next-button')
nextbutton.click()

# Step 11: Click the "Place Order" button
placeorderbutton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/button[@data-tip="Place Order"]')))
placeorderbutton.click()

def wait_for_element_by_name(self, element_name):
return WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[@{element_name}][!]')
```def test_checkout(self):
# Step 1: Open home page
self.driver.get(self.url)

# Step 2: Click on product category
category_button = self.wait_for_element_by_name('product-categories')
category_button.click()

# Step 3: Select the first product
first_product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/a')))
first\_product.click()
```        # Step 4: Click the cart icon/button to open the shopping bag
cart_icon_button = self.wait_for_element_by_name('cart-button')
cart\_icon\_button.click()

# Step 5: Verify that the "GO TO CHECKOUT" button is present inside the cart
checkoutbutton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[1]/button[@data-tip="View Cart"]')))
assert\_true(checkoutbutton)

# Step 6: Click the "GO TO CHECKOUT" button
checkoutbutton.click()

# Step 7: Wait for the checkout form to appear
checkoutform = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[1]/form')))

# Step 8: Fill out the checkout form fields using the following credentials:
email\_input = self.wait_for_element_by_name('email')
email\_input.send_keys('mail@mail.com')

phone\_input = self.wait_for_element_by_name('phone')
phone\_input.send_keys(12345678)

state\_input = self.wait\_for\_element\_by\_name('state')
state\_input.select\_by\_value('Riga')

city\_input = self.wait\_for\_element\_by\_name('city')
city\_input.send\_keys('Riga')

# Step 9: Select a shipping method and a payment method
shipping\_method\_select = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/select[@name="shipping-method"]')))
payment\_method\_select = WebDriverWait(self.driver, 20).until(EC.element\_located((By.XPATH, f'//*[1]/select[@name="payment-method"]')))

# Step 10: Click the "Next" button
nextbutton = self.wait\_for\_element\_by\_name('next-button')
nextbutton.click()

# Step 11: Click the "Place Order" button
placeorderbutton = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/button[@data-tip="Place Order"]')))
placeorderbutton.click()
```    def test\_checkout(self):
        # Step 1: Open home page
        self.driver.get(self.url)

        # Step 2: Click on product category
        category_button = self.wait\_for\_element\_by\_name('product-categories')
        category\_button.click()

        # Step 3: Select the first product
        first\_product = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/a')))
        first\_product.click()
```    \# Step 4: Click the cart icon/button to open the shopping bag
cart\_icon\_button = self.wait\_for\_element\_by\_name('cart-button')
cart\_icon\_button.click()

# Step 5: Verify that the "GO TO CHECKOUT" button is present inside the cart
checkoutbutton = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/button[@data-tip="View Cart"]')))
assert\_true(checkoutbutton)

# Step 6: Click the "GO TO CHECKOUT" button
checkoutbutton.click()

# Step 7: Wait for the checkout form to appear
checkoutform = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/form')))

# Step 8: Fill out the checkout form fields using the following credentials:
email\_input = self.wait\_for\_element\_by\_name('email')
email\_input.send\_keys('mail@mail.com')

phone\_input = self.wait\_for\_element\_by\_name('phone')
phone\_input.send\_keys(12345678)

state\_input = self.wait\_for\_element\_by\_name('state')
state\_input.select\_by\_value('Riga')

city\_input = self.wait\_for\_element\_by\_name('city')
city\_input.send\_keys('Riga')

# Step 9: Select a shipping method and a payment method
shipping\_method\_select = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, f'//*[1]/select[@name="shipping-method"]')))
payment\_method\_select = WebDriverWait(self.driver, 20).until(EC.element\_located((By.XPATH, f'///*[1]/select[@name="payment-method"]')))

# Step 10: Click the "Next" button
nextbutton = self.wait\_for\_element\_by\_name('next-button')
nextbutton.click()

# Step 11: Click the "Place Order" button
placeorderbutton = WebDriverWait(self.driver, 20).until(EC.element\_located((By.XPATH, f'///*[1]/button[@data-tip="Place Order"]'))))
placeorderbutton.click()
```    test\_checkout()

if \_\_\_\_\_\_\_name\_\_\_\_\_\_\_\_\_\_main\_\_\_\_\_\_\_\_\_\_\_ == '\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\