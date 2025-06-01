import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.color import By
from selenium.webdriver.support.wait import Until
from selenium.webdriver.support.ui import WebDriverWait

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://max/register?returnUrl=%2F'

    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        self.driver.get(self.url)

        # Check that the main UI components are present
        self.assertTrue(self.driver.find_element_by_id('header'))
        self.assertTrue(self.driver.find_element_by_name('email'))
        self.assertTrue(self.driver.find_element_by_name('password'))
        self.assertTrue(self.driver.find_element_by_name('returnUrl'))

        # Check that these elements exist and are visible
        self.assertTrue(self.driver.find_element_by_id('register-header'))
        self.assertTrue(self.driver.find_element_by_name('register-email'))
        self.assertTrue(self.driver.find_element_by_name('register-password'))
        self.assertTrue(self.driver.find_element_by_name('register-returnUrl'))

        # Use WebDriverWait to manage time-outs
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'header')))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'email')))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'password')))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'returnUrl')))

if __name__ == '__main__':
    unittest.main()