from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSelenium(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
self.driver.get("http://localhost/")

def tearDown(self):
self.driver.quit()

def test_login_and_fill_address(self):
# Check the login and billing information fields are empty
assert self.is_element_present_by_css_selector(".email")
assert self.is_element_present_by_css_selector(".password")

# Fill in email address and password
email = self.driver.find_element_by_name("email")
password = self.driver.find_element_by_name("password")

email.send_keys("test22@user.com")
password.send_keys("test**11")

# Click on the login button
login_button = self.driver.find_element_by_css_selector(".login-button")
login_button.click()

def is_element_present(self, by, value):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://localhost/")
driver.find_element(by=by, value=value)
return True

if __name__ == '__main__':
unittest.main()