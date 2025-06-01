from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import urllib.request as urllib
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class TestEmailClientSelenium(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.email_client_url = "http://localhost:8080/en/"
art_url = self.email_client_url + "9-art"
clothes_url = self.email_client_url + "3-"
accessories_url = self.email_client_url + "6-"
login_url = self.email_client_url + "login"
register_url = self.email_client_url + "registration"

def tearDown(self):
self.driver.quit()

def test_email_client_selenium(self):

# Check that the main UI components are present
self.assertTrue("header" in self.driver.find_element_by_css_selector(".ui-autocomplete.ui-autocomplete-contents").parent.parent)
self.assertTrue("button" in self.driver.find_element_by_css_selector(".email-client-button")
```less
for url in [art_url, clothes_url, accessories_url, login_url, register_url]:
    # Check that these elements exist and are visible.
    self.assertTrue(url in self.email_client_url)
    self.assertTrue(self.email_client_url + "header" in self.driver.find_element_by_css_selector(".ui-autocomplete.ui-autocomplete-contents").parent.parent)
    self.assertTrue(self.email_client_url + "button" in self.driver.find_element_by_css_selector(".email-client-button"))
    self.assertTrue(self.email_client_url + "form-field" in self.driver.find_element_by_css_selector(".email-client-form-field"))

def test_email_client_selenium(self):

# Check that the main UI components are present
self.assertTrue("header" in self.driver.find_element_by_css_selector(".ui-autocomplete.ui-autocomplete-contents").parent.parent)
self.assertTrue("button" in self.driver.find_element_by_css_selector(".email-client-button")
```less
for url in [art_url, clothes_url, accessories_url, login_url, register_url]:
    # Check that these elements exist and are visible.
    self.assertTrue(url in self.email_client_url)
    self.assertTrue(self.email_client_url + "header" in self.driver.find_element_by_css_selector(".ui-autocomplete.ui-autocomplete-contents").parent.parent)
    self.assertTrue(self.email_client_url + "button" in self.driver.find_element_by_css_selector(".email-client-button"))
    self.assertTrue(self.email_client_url + "form-field" in self.driver.find_element_by_css_selector(".email-client-form-field"))
```