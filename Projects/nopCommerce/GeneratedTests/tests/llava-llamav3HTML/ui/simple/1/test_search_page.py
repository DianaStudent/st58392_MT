import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.keys import Key

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()
    
    def test_home_page(self):
        # Open the homepage
        driver = self.driver
        driver.get('http://max/')
        
        # Check that headers, buttons, links, form fields, etc. are present and visible
        WebDriverWait(driver, 20).until(
            By.XPATH, "//h1[contains(text(), 'Max')]"))
        driver.find_element_by_name('q').send_keys('test')
        
    def test_login_page(self):
        # Open the login page
        driver = self.driver
        driver.get('http://max/login?returnUrl=%2F')
        
        # Check that headers, buttons, links, form fields, etc. are present and visible
        WebDriverWait(driver, 20).until(
            By.XPATH, "//h1[contains(text(), 'Login')]"))
        driver.find_element_by_name('email').send_keys('test@example.com')
        driver.find_element_by_name('password').send_keys('test1234')
        
    def test_register_page(self):
        # Open the register page
        driver = self.driver
        driver.get('http://max/register?returnUrl=%2F')
        
        # Check that headers, buttons, links, form fields, etc. are present and visible
        WebDriverWait(driver, 20).until(
            By.XPATH, "//h1[contains(text(), 'Register')]"))
        driver.find_element_by_name('email').send_keys('test@example.com')
        driver.find_element_by_name('password').send_keys('test1234')

if __name__ == '__main__':
    unittest.main()