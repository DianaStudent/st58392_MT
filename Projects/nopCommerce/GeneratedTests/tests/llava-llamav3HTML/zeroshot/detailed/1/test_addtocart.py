import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.errorhandling import UnexpectedAlertException
from selenium.webdriver.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.exceptions import NoNewSessionKey
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.logging import log_to

def setUp(self):
log_to('test.log', level='INFO')
self.driver = webdriver.Chrome()
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_search_book(self):
try:
self.wait.until(EC.visibility_of_element_located((By.ID, 'search-box')))
search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'search-box')))
search_box.send_keys('book')
search_box.send_keys(Keys.RETURN)

self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'product-grid')]")))
first_product = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class,'product-image-link')][1]")))
first_product_image = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@class,'product-image')]")))

self.wait.until(EC.visibility_of_element_located((By.ID, 'shopping-cart')))
cart_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class,'shopping-cart-link')][1]")))
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(@for,'update-cart-quantity')]")))

self.wait.until(EC.visibility_of_element_located((By.ID, 'total')))
total_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'amount'])]")))
assert total_page.text.strip() != '0.00', f'Expected: <{total}>'
assert first_product_image.source == 'data:image/jpeg;base64,iVBSE...w=='; # Check the image source URL
assert 'The product has been added to your shopping cart.' in self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'shopping-cart-message')]"))).text

except UnexpectedAlertException as e:
self.fail(f'Unexpected alert: {e.text}')

except NoNewSessionKey as e:
self.fail(f'Error initializing driver: {e.message}')