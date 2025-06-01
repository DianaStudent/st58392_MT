from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as WebWait
from selenium.webdriver.support.ui import Select as SeleniumSelect
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestAddToCartProcess(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.driver.get('http://localhost:8080/en/')
self.art_category = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@href='/en/ART']")))

def tearDown(self):
self.driver.quit()

def test_add_to_cart_process(self):
# Step 1
art_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//nav/li/a[@href='/en/ART']"))
)
art_button.click()

# Step 2
category_page = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'menu')]/a[@role='button']")
))
category_page.click()

# Step 3
first_product = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//a[contains(@class,'product-name')][1]"))
)
first_product.click()

# Step 4
add_to_cart_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
add_to_cart_button.click()

# Step 5
modal_popup = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'modal modal-absolute modal-overflow modal-open modal-show modal-open')][1]"))
)

success_message = WebDriverWait(modal_popup, 20).until(
EC.element_located((By.XPATH,
"//span[contains(text,'successfully added')]"))
)
self.assertEqual(success_message.text, "Successfully added", msg="Failed to see the success message.")

if 'proceed_to_checkout' is not visible:
pass
else:
proceed_button = WebDriverWait(modal_popup, 20).until(
EC.element_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
proceed_button.click()

# Step 7
self.assertEqual(art_category, 'ART', msg="Incorrect category")
self.assertTrue('ART' in self.art_category.text)

def test_add_to_cart_process(self):
# Step 1
art_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//nav/li/a[@href='/en/ART']"))
)
art_button.click()

# Step 2
category_page = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'menu')]/a[@role='button']")
))
category_page.click()

# Step 3
first_product = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//a[contains(@class,'product-name')][1]"))
)
first_product.click()

# Step 4
add_to_cart_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
add_to_cart_button.click()

# Step 5
modal_popup = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'modal modal-absolute modal-overflow modal-open modal-show modal-open')][1]"))
)

success_message = WebDriverWait(modal_popup, 20).until(
EC.element_located((By.XPATH,
"//span[contains(text,'successfully added')]"))
)
self.assertEqual(success_message.text, "Successfully added", msg="Failed to see the success message.")

if 'proceed_to_checkout' is not visible:
pass
else:
proceed_button = WebDriverWait(modal_popup, 20).until(
EC.element_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
proceed_button.click()

# Step 6
self.assertEqual(art_category, 'ART', msg="Incorrect category")
self.assertTrue('ART' in self.art_category.text)

if name != 'TestAddToCartProcess':
pass

def test_add_to_cart_process(self):
# Step 1
art_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//nav/li/a[@href='/en/ART']"))
)
artbutton = SeleniumSelect(self.art_category, 'a')
art_button.select_by_text('ART')

# Step 2
category_page = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'menu')]/a[@role='button']")
))
category_page = SeleniumSelect(category_page, 'a')
category_page.select_by_text('ART')

# Step 3
first_product = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//a[contains(@class,'product-name')][1]"))
)
firstproduct = SeleniumSelect(first_product, 'div')
first_product = SeleniumSelect(first_product, 'div', 'data-attribute')
first_product.select_by_text('TestAddToCartProcess')

# Step 4
add_to_cart_button = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
add_to_cart_button = SeleniumSelect(add_to_cart_button, 'a')
add_to_cart_button.click()

# Step 5
modal_popup = WebDriverWait(self.driver, 20).until(
EC.element_located((By.XPATH,
"//div[contains(@class,'modal modal-absolute modal-overflow modal-open modal-show modal-open')][1]"))
)

success_message = WebDriverWait(modal_popup, 20).until(
EC.element_located((By.XPATH,
"//span[contains(text,'successfully added')]"))
)
self.assertEqual(success\_message.text, "Successfully added", msg="Failed to see the success message.")

if 'proceed\_to\_checkout' is not visible:
pass
else:
proceed\_button = WebDriverWait(modal\_popup, 20).until(
EC.element\_located((By.XPATH,
"//button[contains(@data-event-action,'click')]"))
)
proceed\_button = SeleniumSelect(proceed\_button, 'a')
proceed\_button.click()

# Step 7
self.assertEqual(art\_category, 'ART', msg="Incorrect category")
self.assertTrue('ART' in self.art\_category.text)