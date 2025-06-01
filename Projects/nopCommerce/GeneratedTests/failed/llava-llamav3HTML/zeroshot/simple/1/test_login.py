from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestLogin(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_login(self):
# Load the login page
page_title = self.wait_for_page_title("Welcome, Please Sign In!")
self.assertEqual(page_title,"Welcome, Please Sign In!")

# Fill in the email and password fields with valid credentials
email_field = self.wait_for_element_by_name("Email")
password_field = self.wait_for_element_by_name("Password")
email_field.send_keys("admin@admin.com")
password_field.send_keys("admin")

# Click the Log in button to submit the login form
login_button = self.wait_for_element_by_name("Login")
self.driver.execute_script('arguments[0].click();', login_button)

# Verify that the logout button is present in the top navigation
logout_button = self.wait_for_element_by_css_selector(".administration")

# Check for any missing required elements
if not logout_button:
self.fail("No 'logout' button found in the 'logout' section")
elif page_title != "Welcome, Please Sign In!":
self.fail("Page title is incorrect after login")

def wait_for_page_title(self, expected):
return WebDriverWait(self.driver, 20).until(lambda driver: driver.title == expected)
def wait_for_element_by_name(self, name):
return WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_name(name))
def wait_for_element_by_css_selector(self, selector):
return WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_css_selector(selector))

if __name__ == '__main__':
unittest.main()