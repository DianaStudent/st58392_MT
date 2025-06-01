from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

class TestShopperWebsite(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

def test_shopper_website(self):
# Step 1: Open the page.
self.driver.get("http://localhost/")

# Step 2: Confirm the presence of key interface elements: navigation links, inputs, buttons, banners.
self.assertTrue(self.driver.find_element_by_tag_name("nav"))
self.assertTrue(self.driver.find_element_by_tag_name("h1"))

# Step 3: Interact with one or two elements — e.g., click a button and check that the UI updates visually.
button = self.driver.find_element_by_id("button-id")
button.click()
self.assertTrue(self.driver.find_element_by_text("Button text has changed"))

form = self.driver.find_element_by_name("form-name")
select = Select(form)
select.select_by_value("value-id")
self.assertTrue(self.driver.find_element_by_text("Selection text has changed"))

# Step 4: Verify that interactive elements do not cause errors in the UI.
try:
WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "button-id")))
except NoSuchElementException as e:
self.fail(f"Button with ID 'button-id' not found")

try:
WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "form-name")))
except NoSuchElementException as e:
self.fail(f"Form with name 'form-name' not found")

# If any required element is missing, fail the test using self.fail(...).
if not self.driver.find_element_by_id("header-id"):
self.fail(f"Header with ID 'header-id' not found")