from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
class TestMax(unittest.TestCase):
def setUp(self):
# Set the timeout for the wait element to 20 seconds
WebDriverWait(self.driver, 20)
# Use a driver manager to manage the ChromeDriver
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver_path())
def tearDown(self):
pass
def test_search_page(self):
# Load the main page
self.driver.get('http://max/')
# Ensure that structural elements (e.g., header, footer, navigation) are visible
if EC.visibility_of_all_elements_located((By.XPATH, 'header'))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Check the presence and visibility of input fields, buttons, labels, and sections
search_input = self.wait_for_element('input[name]')
if search_input:
self.assertTrue(search_input.get_attribute('name') == 'q')
assert(EC.visibility_of_element_located((By.XPATH, 'form')))
assert(EC.visibility_of_element_located((By.XPATH, 'button')))
assert(EC.visibility_of_element_located((By.XPATH, 'label')))
# Interact with key UI elements (e.g., click buttons)
search_input.send_keys('test_search_query')
search_button = self.wait_for_element('input[alt]')
self.assertTrue(search_button.get_attribute('alt') == 'Search button')
search_button.click()
# Confirm that the UI reacts visually
assert(EC.visibility_of_element_located((By.XPATH, 'header')))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Assert that no required UI element is missing
if not EC.presence_of_all_elements_located((By.XPATH, 'header')))
self.fail('Header element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'footer')))
self.fail('Footer element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'nav')))
self.fail('Nav element is missing')
def test_login_page(self):
# Load the login page
self.driver.get('http://max/login?returnUrl=%2F')
# Ensure that structural elements (e.g., header, footer, navigation) are visible
if EC.visibility_of_all_elements_located((By.XPATH, 'header'))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Check the presence and visibility of input fields, buttons, labels, and sections
login_input = self.wait_for_element('input[name]')
if login_input:
self.assertTrue(login_input.get_attribute('name') == 'username')
password_input = self.wait_for_element('input[type="password"]')
assert(EC.visibility_of_element_located((By.XPATH, 'form')))
assert(EC.visibility_of_element_located((By.XPATH, 'button')))
assert(EC.visibility_of_element_located((By.XPATH, 'label')))
# Interact with key UI elements (e.g., click buttons)
login_input.send_keys('test_username')
password_input.send_keys('test_password')
login_button = self.wait_for_element('input[alt]')
self.assertTrue(login_button.get_attribute('alt') == 'Login button')
login_button.click()
# Confirm that the UI reacts visually
assert(EC.visibility_of_element_located((By.XPATH, 'header')))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Assert that no required UI element is missing
if not EC.presence_of_all_elements_located((By.XPATH, 'header')))
self.fail('Header element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'footer')))
self.fail('Footer element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'nav')))
self.fail('Nav element is missing')
def test_register_page(self):
# Load the register page
self.driver.get('http://max/register?returnUrl=%2F')
# Ensure that structural elements (e.g., header, footer, navigation) are visible
if EC.visibility_of_all_elements_located((By.XPATH, 'header'))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Check the presence and visibility of input fields, buttons, labels, and sections
register_input = self.wait_for_element('input[name]')
if register_input:
self.assertTrue(register_input.get_attribute('name') == 'email')
password_input = self.wait_for_element('input[type="password"]')
assert(EC.visibility_of_element_located((By.XPATH, 'form')))
assert(EC.visibility_of_element_located((By.XPATH, 'button')))
assert(EC.visibility_of_element_located((By.XPATH, 'label')))
# Interact with key UI elements (e.g., click buttons)
register_input.send_keys('test_email')
password_input.send_keys('test_password')
register_button = self.wait_for_element('input[alt]')
self.assertTrue(register_button.get_attribute('alt') == 'Register button')
register_button.click()
# Confirm that the UI reacts visually
assert(EC.visibility_of_element_located((By.XPATH, 'header')))
assert(EC.visibility_of_element_located((By.XPATH, 'footer')))
assert(EC.visibility_of_element_located((By.XPATH, 'nav')))
# Assert that no required UI element is missing
if not EC.presence_of_all_elements_located((By.XPATH, 'header')))
self.fail('Header element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'footer')))
self.fail('Footer element is missing')
elif not EC.presence_of_all_elements_located((By.XPATH, 'nav')))
self.fail('Nav element is missing')

if name != 'test':
# Load the search page
test_search_page()
# Load the login page
test_login_page()
# Load the register page
test_register_page()

if __name__ == '__main__':
unittest.main()