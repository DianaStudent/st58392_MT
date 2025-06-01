from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

class MaxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

    def test_main_page(self):
        driver = self.driver
        driver.get('http://max/')
        self.assertTrue('header' in driver.title)

    def test_login_page(self):
        driver = self.driver
        driver.get('http://max/login?returnUrl=%2F')
        self.assertTrue('form' in driver.page_source)
        login_username = driver.find_element_by_name('username')
        login_password = driver.find_element_by_name('password')
        login_button = driver.find_element_by_name('loginButton')

    def test_register_page(self):
        driver = self.driver
        driver.get('http://max/register?returnUrl=%2F')
        self.assertTrue('form' in driver.page_source)
        first_name = driver.find_element_by_name('firstName')
        last_name = driver.find_element_by_name('lastName')
        email = driver.find_element_by_name('email')
        phone = driver.find_element_by_name('phone')

    def test_search_page(self):
        driver = self.driver
        driver.get('http://max/search')
        self.assertTrue('form' in driver.page_source)
        search_box = driver.find_element_by_name('searchBox')
        search_button = driver.find_element_by_name('searchButton')

if __name__ == '__main__':
    unittest.main()