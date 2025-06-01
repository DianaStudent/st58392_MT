from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import UiSelector
import time
import HtmlElement
from page_objects import HomePage, CategoryPage, Category1Page
class TestHomePage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()
def test_homepage(self):
# Load the page and ensure that structural elements (e.g., header, footer, navigation) are visible.
WebDriverWait(self.driver, 20).until(
UiSelector(".header"),
UiSelector(".footer")
)
assert UiSelector(".header").is_present()
assert UiSelector(".footer").is_present()

# Check the presence and visibility of input fields, buttons, labels, and sections.
input_search = HtmlElement(".search-input-field", self.driver)
button_search = HtmlElement(".search-button", self.driver)

assert input_search.is_element_located() == True
assert button_search.is_element_located() == True

assert UiSelector(".category-list").is_present()
for category in ["Category A", "Category B"]:
page = CategoryPage(self.driver, category)
assert page.is_category_page()

# Interact with key UI elements (e.g., click buttons).
button_search.click()

# Confirm that the UI reacts visually.
time.sleep(1)

assert UiSelector(".category-list").is_present()
for category in ["Category A", "Category B"]:
page = CategoryPage(self.driver, category)
assert page.is_category_page()

# Check if all categories are present
categories = []
for category in ["Category A", "Category B"]:
page = CategoryPage(self.driver, category)
categories.append(page.get_name())

assert len(categories) == 2

# Test the footer
UiSelector(".footer").click()
time.sleep(1)

assert UiSelector(".my-account-link").is_present()

def test_category_a_page(self):
category_1 = HtmlElement(".category-a", self.driver)
assert category_1.is_element_located() == True

for category in ["Category A-1", "Category B"]:
page = Category1Page(self.driver, category)
assert page.is_category1_page()

# Test the footer
UiSelector(".footer").click()
time.sleep(1)

assert UiSelector(".my-account-link").is_present()

if __name__ == '__main__':
unittest.main()