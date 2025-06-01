import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.element import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import DriverWrapper

class TestMaxWebsite(unittest.TestCase):
def setUp(self):
self.driver = ChromeDriverManager().get_driver()
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_max_website(self):
try:
# navigate to the home page
self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//a[@title='Home']")))
# check that all required elements are visible and present
self.assertTrue(self.home_xpath_exists(), 'Required element not found')
self.assertTrue(self.login_xpath_exists(), 'Required element not found')
self.assertTrue(self.register_xpath_exists(), 'Required element not found')
self.assertTrue(self.search_xpath_exists(), 'Required element not found')

def home_xpath_exists():
# check that the main UI components are present
return self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//h1[@class='page-title']")))
self.assertTrue(self.headers_header_tag_invisible())

def login_xpath_exists():
# navigate to the login page
self.driver.get(self.login_page)
self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//input[@type='text'@name='username'@placeholder='Username...']")))
return self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//input[@type='password'@name='password'@placeholder='Password...]')))
self.assertTrue(self.headers_header_tag_invisible())

def register_xpath_exists():
# navigate to the registration page
self.driver.get(self.register_page)
self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//input[@type='text'@name='firstName'@placeholder='First Name...']")))
return self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//input[@type='text'@name='lastName'@placeholder='Last Name...']")))
self.assertTrue(self.headers_header_tag_invisible())

def search_xpath_exists():
# navigate to the search page
self.driver.get(self.search_page)
self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//input[@type='text'@name='searchKeyword'@placeholder='Search Keyword...']")))
return self.wait.until(ExpectedConditions.visibilityOfElementLocated(By.XPATH, "//select[@name='categories']"))))

def headers_header_tag_invisible():
# check that the <header> tag is not visible
header = self.wait.until(ExpectedConditions.invisibilityOfElementLocated(By.XPATH, "//h1[@class='page-title']")))
return header.is_invisible()

if __name__ == '__main__':
unittest.main()