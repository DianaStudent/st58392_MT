from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from html_ data import html_data
class TestShoppingOrder(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
def tearDown(self):
self.driver.quit()
def test\_shopping_order(self):
# 1. Open home page.
self.driver.get(html\_data.HOME\_PAGE)
# 2. Click on product category.
product_category = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.PRODUCT\_CATEGORY)))
product\_category.click()
# 3. Select the first product.
product = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.FIRST\_PRODUCT)))
product.click()
# 4. Click the  "Add to cart" button.
add\_to\_cart = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.ADD\_TO\_CART)))
add\_to\_cart.click()
# 5. Click the cart icon/button to open the shopping bag.
shopping\_bag = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.CART\_BUTTON)))
shopping\_bag.click()
# 6. Verify that the  "GO TO CHECKOUT" button is present inside the cart.
go\_to\_checkout = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.GO\_TO\_CHECKOUT)))
self.assertEqual(go\_to\_checkout.get\_attribute('href'), html\_data.GO\_TO\_CHECKOUT)
# 7. Click the  "GO TO CHECKOUT" button.
go\_to\_checkout.click()
# 8. Wait for the checkout form to appear.
checkout = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.CHECKOUT)))
# 9. Fill out the checkout form fields using the following credentials:
email\_field = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.EMAIL\_FIELD)))
phone\_field = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.PHONE\_FIELD)))
state\_field = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.STATE\_FIELD)))
city\_field = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.CITY\_FIELD)))
email\_field.send\_keys("mail@mai l.com")
phone\_field.send\_keys("12345678")
state\_field.send\_keys("Riga")
city\_field.send\_keys("Riga")
# 10. Select a shipping method and a payment method.
shipping\_method = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.S SHIPPING\_METHOD)))
payment\_method = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.PAYMENT\_METHOD)))
shipping\_method.click()
payment\_method.click()
# 11. Click the  "Next" button.
next = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.NEXT)))
next.click()
# 12. Click the  "Place Order" button.
place\_order = WebDriverWait(self.driver, 20).until(EC.element\_to\_be\_clickable((By.XPATH, html\_data.PLACE\_ORDER)))
place\_order.click()
# 13. Wait for the confirmation page and check that it includes the text  "Thanks for your order!". \
success\_page = WebDriverWait(self.driver, 20).until(EC.text\_contains('Thanks for your order!', visible=True))
self.assertEqual(success\_page, "Thanks for your order!")
if self.assertTrue(email\_field.get\_attribute('value') != html\_data.EMAIL,
phone\_field.get\_attribute('value') != html\_data.PHONE,
state\_field.get\_attribute('value') != html\_data.STATE,
city\_field.get\_attribute('value') != html\_data.CITY,
print("Test failed")
else:
print("Test passed")