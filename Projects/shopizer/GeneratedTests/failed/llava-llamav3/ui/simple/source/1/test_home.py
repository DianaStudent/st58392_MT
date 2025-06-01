from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestShopFurn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home(self):
        self.assertTrue(self.driver.current_url == "http://localhost/")
        time.sleep(2)

    def test_tables(self):
        self.driver.get("http://localhost/category/tables")
        time.sleep(2)
        self.assertTrue(self.driver.current_url == "http://localhost/category/tables")

    def test_chairs(self):
        self.driver.get("http://localhost/category/chairs")
        time.sleep(2)
        self.assertTrue(self.driver.current_url == "http://localhost/category/chairs")

    def test_login(self):
        self.driver.get("http://localhost/login")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()