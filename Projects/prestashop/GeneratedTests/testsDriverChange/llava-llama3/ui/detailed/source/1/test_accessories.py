import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcomWebsite(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def tearDown(self):
self.driver.quit()

def test_page_load(self):
self.driver.get("http://localhost:8080/en/")
assert(self.driver.title == "E-commerce")

def test_clothes_category(self):
self.driver.get("http://localhost:8080/en/3-clothes")
assert(self.driver.title == "Clothes - E-commerce")

def test_accessories_category(self):
self.driver.get("http://localhost:8080/en/6-accessories")
assert(self.driver.title == "Accessories - E-commerce")

def test_art_category(self):
self.driver.get("http://localhost:8080/en/9-art")
assert(self.driver.title == "Art - E-commerce")

def test_login_page(self):
self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
assert(self.driver.title == "Login - E-commerce")

def test_register_page(self):
self.driver.get("http://localhost:8080/en/registration")
assert(self.driver.title == "Register - E-commerce")

if __name__ == '__main__':
unittest.main()