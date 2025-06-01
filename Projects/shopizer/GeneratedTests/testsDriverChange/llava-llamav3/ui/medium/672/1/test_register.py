from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import ChromeDriverManager
from selenium.webdriverv6.core.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager import DriverWrapper

class TestShopperRegistrationPage(unittest.TestCase):
def setUp(self):
self.driver = self.create_driver()

def tearDown(self):
self.driver.quit()

def create_driver(self):
driver_manager = DriverWrapper(ChromeDriverManager())
options = Options()
options.add_argument("window-size=1920,1080")
return Chrome(options=options)

def test_shopper_registration_page(self):
try:
self.assertEqual(self.driver.current_url, "http://localhost/register")
elements = self.driver.find_elements_by_css_selector(".form-control")
for element in elements:
if not element.get_attribute("name"):
print(f"Element name: {element.get_attribute('id')}")
else:
print(f"Element name: {element.get_attribute('name')}")

# Check that the main UI components are present
self.assertTrue(self.driver.find_element_by_css_selector(".header"))
self.assertTrue(self.driver.find_element_by_css_selector(".logo"))
self.assertTrue(self.driver.find_element_by_css_selector(".copyright"))
self.assertTrue(self.driver.find_element_by_css_selector(".register-form"))

# Check that these elements exist and are visible
if not self.driver.find_elements_by_css_selector(".first-name"):
self.fail("First name input is missing")
if not self.driver.find_elements_by_css_selector(".last-name"):
self.fail("Last name input is missing")

# Verify that interactive elements do not cause errors in the UI
button = self.driver.find_element_by_css_selector(".btn-register")
(self.wait_until_clickable(button), f"Button 'register' failed to be clickable after 20 seconds")
button.click()

(self.wait_until_clickable(self.driver.find_element_by_css_selector(".form-control.first-name")), f"First name input failed to appear after 20 seconds")
(self.wait_until_clickable(self.driver.find_element_by_css_selector(".form-control.last-name")), f"Last name input failed to appear after 20 seconds")
(self.wait_until_clickable(self.driver.find_element_by_css_selector(".form-control.email-address")), f"Email address input failed to appear after 20 seconds")

# Check that the website displays its copyright information
self.assertEqual(self.driver.current_url, "http://localhost/")
self.assertTrue(self.driver.find_element_by_css_selector(".copyright"))

if __name__ == "__main__":
unittest.main()