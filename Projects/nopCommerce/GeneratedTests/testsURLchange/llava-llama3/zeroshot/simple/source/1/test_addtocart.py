from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from webdriver_manager import DriverWrapper
import html_data

class TestSearchBook(TestCase):
def setUp(self):
self.driver = DriverWrapper.Chrome()

def tearDown(self):
self.driver.quit()
def test_search_book(self):
self.search_box = self.driver.find_element_by_name("search")
# Add a book in the search box and submit the search form
self.search_box.send_keys(html_data.BOOK_NAME)
self.search_box.submit()
# Wait for the success notification to appear
success_notification = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "div[contains(text(), 'Product successfully added to cart.')]")))
success_link = self.success_notification.find_element_by_tag_name("a")
# Check if the cart contains at least one item
if self.success_link is None:
self.fail("The cart does not contain any items.")
else:
item_count = self.cart_page.find_element_by_xpath("//tr[contains(text(), '1')]/td[2]").text.strip()
if item_count == "0":
self.fail("The cart is empty.")
else:
pass

def tearDown(self):
self.driver.quit()