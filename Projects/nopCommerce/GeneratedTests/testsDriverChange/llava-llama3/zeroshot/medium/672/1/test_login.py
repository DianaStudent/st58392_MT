from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class LoginTest(TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_login(self):
# Home page
self.driver.get("http://max/")
self.wait_for_element_located((By.XPATH, "//*[@name='__RequestVerificationToken']"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Welcome to our store')]"))

# Login page
self.driver.find_element_by_name("Email").send_keys("admin@admin.com")
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email')]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email')]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email')]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email')]"))

# Enter password
self.driver.find_element_by_name("Password").send_keys("admin")

# Login button
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'login')]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email')]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email)]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email)]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email)]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email)]"))
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Wrong email)]"))

# Verify login
self.wait_for_element_located((By.XPATH, "//*[contains(text(), 'Log out')]"))