import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.action import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegisterPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_register_page(self):
# Load the page and ensure that structural elements (e.g., header, footer, navigation) are visible.
self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text('register'))]")))
# Check the presence and visibility of input fields, buttons, labels, and sections.
form = self.wait.until(EC.presence_of_element_located((By.ID, 'default')))
fields = form.find_elements_by_xpath("//*[contains(text('username'))]")
self.assertEqual(len(fields), 1)
password_fields = form.find_elements_by_xpath("//*[contains(text('password'))]")
self.assertEqual(len(password_fields), 2)
# Interact with key UI elements (e.g., click buttons).
button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text('register'))]")))
button.click()
if self.driver.current_url != 'http://localhost/register':
self.fail("Register button did not redirect to the register page.")

# Confirm that the UI reacts visually.
if self.driver.title != 'Shopify Registration Page':
self.fail("UI did not change after interacting with the register button.")

if len(self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text('default'))]")))) == 0:
self.fail("Register form was not displayed after clicking the register button.")

# Assert that no required UI element is missing.
if 'shopify' not in self.driver.page_source:
self.fail("Shopify was not mentioned anywhere on the page.")
if 'register' not in self.driver.page_source:
self.fail("Register was not mentioned anywhere on the page.")

if 'username' not in self.driver.page_source:
self.fail("Username field was not displayed on the page.")
if 'password' not in self.driver.page_source:
self.fail("Password fields were not displayed on the page.")
if 'terms of service' not in self.driver.page_source:
self.fail("Terms of service were not mentioned anywhere on the page.")

if 'chairs' not in self.driver.page_source:
self.fail("Chairs were not mentioned anywhere on the page.")
if 'tables' not in self.driver.page_source:
self.fail("Tables were not mentioned anywhere on the page.")

if 'login' not in self.driver.page_source:
self.fail("Login was not mentioned anywhere on the page.")

# Return only Python code using unittest.