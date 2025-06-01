import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assertions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.fileupload import FileUpload

class TestArtAndDesignRegistration(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_load_page(self):
self.assertEqual(self.driver.title, "Art & Design", "Page Title is incorrect")
self.assertTrue(self.driver.find_element_by_tag_name("header").is_displayed())
self.assertTrue(self.driver.find_element_by_tag_name("footer").is_displayed())
self.assertTrue(self.driver.find_element_by_tag_name("nav").is_displayed())

def test_ui_elements(self):
# Check that the main UI components are present
assert self.driver.find_element_by_tag_name("h1").is_displayed()
assert self.driver.find_element_by_tag_name("button").is_displayed()
assert self.driver.find_element_by_tag_name("input").is_displayed()

# Check that these elements exist and are visible
assert self.driver.find_element_by_tag_name("h1").is_displayed()
assert self.driver.find_element_by_tag_name("button").is_displayed()
assert self.driver.find_element_by_tag_name("input").is_displayed()

def test_ui_interactions(self):
# Click on the "Enroll Now" button
self.driver.find_element_by_css_selector(".btn-enroll.now > a").click()

# Check that the page is redirected to the course registration page
self.assertEqual(self.driver.url, "http://localhost:8080/registration")

# Interact with key UI elements
self.driver.find_element_by_css_selector(".cart-add > a").click()
self.wait = WebDriverWait(self.driver, 20)

def test_ui_reactions(self):
# Check that the visual UI reacts to user interactions
assert self.driver.find_element_by_css_selector(".cart-add > a").is_displayed()

def test_required_elements(self):
assert self.driver.find_element_by_css_selector("h1").is_displayed()
assert self.driver.find_element_by_css_selector("button").is_displayed()
assert self.driver.find_element_by_css_selector("input").is_displayed()

if __name__ == '__main__':
unittest.main()