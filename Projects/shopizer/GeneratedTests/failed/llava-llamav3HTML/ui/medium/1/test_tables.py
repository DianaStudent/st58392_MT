from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from html_data import get_interface_elements, get_required_element_keys, HTMLInterfaceElements

class TestSelenium(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.wait = WebDriverWait(self.driver, 20)
self.html_interface_elements = get_interface_elements()

def tearDown(self):
self.driver.quit()

def test_selenium(self):
# Step 1: Open the page
self.driver.get("http://localhost/")
self.wait.until(EC.element_to_be_clickable((HTMLInterfaceElements.NAVIGATION_LINKS[0], 'id')))
self.wait.until(EC.element_to_be_clickable((HTMLInterfaceElements.NAVIGATION_LINKS[2], 'id')))

# Step 2: Confirm the presence of key interface elements
for element in self.html_interface_elements:
if not self.wait.until(EC.presence_of_element_located((element, 'id'))):
self.fail(f"Element {element} is missing")

# Step 3: Interact with one or two elements
button = self.driver.find_element_by_id(HTMLInterfaceElements.BUTTONS[0])
self.wait.until(EC.element_to_be_clickable(button))
button.click()

input = self.wait.until(EC.element_to_be_clickable((HTMLInterfaceElements.FORM_FIELDS[0], 'id')))
self.wait.until(EC.element_to_be_clickable(input))
input.send_keys("example")
input.submit()

# Step 4: Verify that interactive elements do not cause errors in the UI
error_message = self.wait.until(EC.presence_of_element_located((HTMLInterfaceElements.ERROR_MESSAGES[0], 'id')))

self.assertEqual(error_message.get_attribute('text'), "Error message")
self.wait.until(EC.presence_of_element_located(error_message))

# Step 5: Check that main UI components are present and visible
for element in self.html_interface_elements:
if not self.wait.until(EC.presence_of_element_located((element, 'id'))):
self.fail(f"Element {element} is missing")

if __name__ == '__main__':
unittest.main()