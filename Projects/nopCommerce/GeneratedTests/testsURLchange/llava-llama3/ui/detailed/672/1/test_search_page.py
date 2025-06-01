from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestOnlineStoreSearchPage(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chromeedriver())
        self.driver = driver
        self.url = 'http://max/search'

    def tearDown(self):
        self.driver.quit()

    def test_search_page(self):
        self.driver.get(self.url)
        self.wait_for_element_present('header')
        self.wait_for_element_present('search-form')

        search_form = self.driver.find_element_by_name('search-form')
        search_input = search_form.find_elements_by_name('input[type="text"]')[0]
        select_type = search_form.find_elements_by_name('select[name="filter-type"]')[0]

        for key in key_words:
            select_type.select_by_value(key)
            search_input.send_keys(key)
            self.wait_for_element_present(f'{key}')
            self.wait_for_element_present(f'product-{key}')

def key_words():
    return [
        'Test1',
        'Test2'
    ]

if __name__ == '__main__':
    unittest.main()