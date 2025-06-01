import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestShopifyWebsite(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager.get())
self.driver.implicitly_wait(20, time=1)
self.driver.set_page_load_timeout(20)

def tearDown(self):
self.driver.quit()

def test_main_ui_components(self):
headers = self.driver.find_elements_by_tag_name('h2')
buttons = self.driver.find_elements_by_tag_name('button')
links = self.driver.find_elements_by_tag_name('a')
form_fields = self.driver.find_elements_by_tag_name('input')

self.assertTrue(len(headers) > 1)
self.assertTrue(len(buttons) > 0)
self.assertTrue(len(links) > 0)
self.assertTrue(len(form_fields) > 0)

def test_required_elements(self):
if not self.driver.title.startswith('Shopify'):
self.fail("The main UI components are not present.")

def test_login_and_register(self):
login_url = "http://localhost:8080/en/login"
register_url = "http://localhost:8080/en/registration"

# Test login
driver = webdriver.Chrome(ChromeDriverManager.get())
driver.implicitly_wait(20, time=1)
driver.set_page_load_timeout(20)

username = driver.find_element_by_id('customer_email')
password = driver.find_element_by_id('customer_password')

# Log in
username.send_keys("test@example.com")
password.send_keys("test123")

# Test register
register_username = driver.find_element_by_id('reg_customer_email')
register_password = driver.find_element_by_id('reg_customer_password')

# Register
register_username.send_keys("test-register@example.com")
register_password.send_keys("test123")

# Close the browser
driver.quit()

if __name__ == '__main__':
unittest.main()