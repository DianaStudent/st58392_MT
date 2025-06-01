import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import AssertionsAs
from webdriver_manager.chrome import ChromeDriverManager

class MaxTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_max_page(self):
self.driver.get('http://max/')

# check the presence of key interface elements
assert self.driver.current_url == 'http://max/'

assert self.wait.until(ExpectedConditions.visible_of_elements)((By.ID, 'header')) > 0

# interact with an element - e.g., click a button and check that the UI updates visually
button = (By.XPATH, "//button[contains(text()='Register')]")

self.wait.until(ExpectedConditions.element_to_be_clickable(button))

register_button = self.driver.find_element(*button)

register_button.click()

assert self.wait.until(ExpectedConditions.visibility_of_element_located((By.ID, 'register'))) > 0

# verify that interactive elements do not cause errors in the UI
assert self.wait.until(ExpectedConditions.attribute_value(*button, 'disabled', 'false'))

def test_login_page(self):
self.driver.get('http://max/login?returnUrl=%2F')

assert self.wait.until(ExpectedConditions.visibility_of_element_located((By.ID, 'login'))) > 0

username = (By.XPATH, "//input[contains(@id,'username')]")

password = (By.XPATH, "//input[contains(@id,'password')]")

self.wait.until(ExpectedConditions.attribute_value(*username, 'required', 'true'))

# check that the required fields exist and are visible
assert self.wait.until(ExpectedConditions.visibility_of_elements((username, password))) > 0

def test_register_page(self):
self.driver.get('http://max/register?returnUrl=%2F')

assert self.wait.until(ExpectedConditions.visibility_of_element_located((By.ID, 'register'))) > 0

email = (By.XPATH, "//input[contains(@id,'email')]")

password = (By.XPATH, "//input[contains(@id,'password')]")

self.wait.until(ExpectedConditions.attribute_value(*email, 'required', 'true'))

# check that the required fields exist and are visible
assert self.wait.until(ExpectedConditions.visibility_of_elements((email, password))) > 0

def test_search_page(self):
self.driver.get('http://max/search')

assert self.wait.until(ExpectedConditions.visibility_of_element_located((By.ID, 'search'))) > 0

search\_field = (By.XPATH, "//input[contains(@id,'search\_field')]")

# check that the search field exists and is visible
assert self.wait.until(ExpectedConditions.attribute_value(*search\_field, 'required', 'true'))

if __name__ == '__main__':
unittest.main()