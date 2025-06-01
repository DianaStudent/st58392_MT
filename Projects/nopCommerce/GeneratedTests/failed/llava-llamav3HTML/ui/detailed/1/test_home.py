from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        self.driver.get('http://max/')
        self.assertTrue(self.driver.find_element_by_tag_name('h1'))
        self.assertTrue(self.driver.find_element_by_tag_name('nav'))

    def test_login_page(self):
        self.driver.get('http://max/login?returnUrl=%2F')
        self.assertTrue(self.driver.find_element_by_name('email'))
        self.assertTrue(self.driver.find_element_by_name('password'))

    def test_register_page(self):
        self.driver.get('http://max/register?returnUrl=%2F')
        self.assertTrue(self.driver.find_element_by_name('firstName'))
        self.assertTrue(self.driver.find_element_by_name('lastName'))
        self.assertTrue(self.driver.find_element_by_name('phone'))

    def test_search_page(self):
        self.driver.get('http://max/search')
        self.assertTrue(self.driver.find_element_by_name('search'))