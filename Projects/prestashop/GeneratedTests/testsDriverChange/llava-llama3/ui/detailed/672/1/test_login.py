import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def tearDown(self):
self.driver.quit()

def test_login_page(self):
try:
WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art'))
assert "Login" in self.driver.title
self.driver.find_element_by_name('email').send_keys('test@example.com')
self.driver.find_element_by_name('password').send_keys('test123')
self.driver.find_element_by_name('Remember me').click()
self.driver.find_element_by_name('Login').click()

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/9-art'))

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art'))
self.driver.find_element_by_name('Forgot Password').click()

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/registration'))

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art'))
self.driver.find_element_by_name('register').click()

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories'))

WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/3-clothes'))
self.driver.find_element_by_name('home').click()
WebDriverWait(self.driver, 20).until(EC.url_to_be('http://localhost:8080/en/'))
except:
self.fail("Test case failed.")

if name == '__main__':
unittest.main()