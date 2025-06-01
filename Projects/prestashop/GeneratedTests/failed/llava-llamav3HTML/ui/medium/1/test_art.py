from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestSelenium(unittest.TestCase):
def setUp(self):
# Set up the ChromeDriver
driver = webdriver.Chrome()

# Go to the main page
self.driver.get("http://localhost:8080/en/")
self.assertEqual(self.driver.title, "PrestaShop - Ecommerce software by PrestaShop")

# Test scenario 1 and 2
self.assertTrue(self.check_elements())
def check_elements(self):
# Check if navigation links exist and are visible
for category in ["clothes", "accessories", "art"]:
url = f"http://localhost:8080/en/{category}"
self.driver.get(url)
self.assertEqual(self.driver.title, f"PrestaShop - {category} - Ecommerce software by PrestaShop")
self.assertTrue(self.check_inputs())
def check_inputs(self):
# Check if inputs exist and are visible
for category in ["clothes", "accessories"]:
url = f"http://localhost:8080/en/{category}"
self.driver.get(url)
self.assertEqual(self.driver.title, f"PrestaShop - {category} - Ecommerce software by PrestaShop")
if self.check_button():
return True

def check_button(self):
# Check if the button exists and is visible
url = "http://localhost:8080/en/9-art"
self.driver.get(url)
self.assertEqual(self.driver.title, "PrestaShop - 9-Art - Ecommerce software by PrestaShop")
button = self.driver.find_element_by_name("submit")
if not (button.is_displayed() and button.is_enabled()):
return False
else:
return True

def tearDown(self):
# Tear down the ChromeDriver
self.driver.quit()

if __name__ == "__main__":
unittest.main()