from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class TestShopizerPage(unittest.TestCase):

def setUp(self):
self.driver = ChromeDriverManager().get_chrome_driver()

def tearDown(self):
self.driver.quit()

def test_main_page(self):
# Check that the main UI components are present: headers, buttons, links, form fields, etc.
header = WebDriverWait(self.driver, 20).until(
EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),\"Shopizer\")]")))
button = WebDriverWait(self.driver, 20).until(
EC.visibility_of_element_located((By.XPATH, "//input[@name=\"submit\"]")))
self.assertEqual(header.text, "Shopizer")
self.assertEqual(button.get_attribute("type"), "submit")

# Check that these elements exist and are visible.
table_category = EC.element_to_be_clickable(EC.by_xpath("//a[contains(text(),\"tables\")"))
chair_category = EC.element_to_be_clickable(EC.by_xpath("//a[contains(text(),\"chairs\")]))
login_button = WebDriverWait(self.driver, 20).until(
EC.visibility_of_element_located((By.XPATH, "//button[contains(text,\"Login\")]")))
registerbutton = WebDriverWait(self.driver, 20).until(
EC.visibility_of_element_located((By.XPATH, "//button[contains(text,\"Register\")]"))))
self.assertTrue(table_category.is_clickable)
self.assertTrue(chair_category.is_clickable)
self.assertTrue(login_button.is_clickable)
self.assertTrue(registerbutton.is_clickable)

# Use unittest with setUp() and tearDown()
self.assertEqual(self.driver.title, "Shopizer")
self.assertEqual(self.driver.current_url, "http://localhost/")

if required_element is missing:
self.fail("Required element is missing")

return True
if __name__== "__main__":
unittest.main()

This code will run a test on the specified website, checking that the main UI components are present and visible. It will use webdriver-manager to manage ChromeDriver and WebDriverWait with a timeout of 20 seconds before interacting with elements. The test will also check the title and URL of the page to ensure they are correct.

Note: This code assumes that the specified website is accessible through the provided URLs (tables, chairs, login, register)