from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.assertions import Assert
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactPage(unittest.TestCase):
def setUp(self):
# Initialize a new browser instance and navigate to the main page.
driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.driver = driver
def tearDown(self):
# Close the browser instance when the test is completed.
self.driver.quit()

def test_main_ui_components(self):
# Check that the main UI components are present.
assert self.driver.find_elements_by_tag_name('h1')
assert self.driver.find_elements_by_tag_name('button')
assert self.driver.find_elements_by_tag_name('a')
assert self.driver.find_elements_by_tag_name('form')

def test_chairs_page(self):
# Navigate to the chairs page and check that it is visible.
self.driver.get('http://localhost/category/chairs')
assert self.driver.title_text().strip() == 'Chairs | shop - react'

def test_login_page(self):
# Navigate to the login page and check that it is visible.
self.driver.get('http://localhost/login')
assert self.driver.title_text().strip() == 'Login | shop - react'

def test_register_page(self):
# Navigate to the register page and check that it is visible.
self.driver.get('http://localhost/register')
assert self.driver.title_text().strip() == 'Register | shop - react'

if __name__ == '__main__':
unittest.main()