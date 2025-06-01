from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

def setUp(self):
# Set up a new session for the browser
driver = webdriver.Chrome("path/to/chromedriver")
self.driver = driver

def tearDown(self):
# Close the browser session
self.driver.quit()

class TestRegister(unittest.TestCase):
def test_register(self):
# Open the home page
self.driver.get("http://localhost/")
assert self.wait_for_element("id", "header-search") != None, "Header search not found"
assert self.wait_for_element("id", "header-cart") != None, "Header cart not found"

# Click on the account button and select "Register"
account_button = self.wait_for_element("id", "header-account")
register_link = account_button.find_element_by_tag_name("a")
register_link.click()

# Fill in the registration form
first_name_field = self.wait_for_element("id", "form-register-first-name")
last_name_field = self.wait_for_element("id", "form-register-last-name")
email_field = self.wait_for_element("id", "form-register-email")
password1_field = self.wait_for_element("id", "form-register-password1")
repeat_password_field = self.wait_for_element("id", "form-register-password2")

first_name_field.send_keys("Test")
last_name_field.send_keys("User")
email_field.send_keys(f"test{unittest.dummy.random.getrandbits(4)}@example.com")
password1_field.send_keys("test**11")
repeat_password_field.send_keys("test**11")

# Select a country and a region/state
select_country = self.wait_for_element("id", "form-register-country-select")
country = select_country.find_elements_by_tag_name("option")[0]
select_region = self.wait_for_element("id", "form-register-region-select")
region = select_region.find_elements_by_tag_name("option")[3]

# Submit the registration form
register_button = self.wait_for_element("id", "form-register-button")

# Wait for redirect and confirm success by checking if the current URL includes "/my-account"
redirect_url = WebDriverWait(self.driver, 20).until(expected=ExpectedConditions.url_contains("/my-account"))

# Tear down the browser session
self tearDown()
assert redirect_url != None, "Redirect to /my-account not found"