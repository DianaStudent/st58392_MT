import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.assertions import Assert

class FilterDetailedTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/category-a')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_filter_detailed(self):
        # Step 1 - Locate and apply the "Brand A" checkbox filter
        wait_for_element_located_and_click(self.wait, "//input[@id='checkbox-0']")
        self.wait.until(ExpectedConditions.visibility_of_all_elements_located,