from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_01_open_page(self):
        self.driver.get("http://localhost:3000")
        self.assertTrue("your logo" in self.driver.title)

    def test_02_verify_category_a(self):
        self.driver.get("http://localhost:3000/category-a")
        self.assertTrue("Category A" in self.driver.title)
        category_a = self.driver.find_element_by_name("category-a")
        category_a_suggestion = self.driver.find_element_by_name("category-a-suggestion")
        self.assertIsNotNone(category_a)
        self.assertIsNotNone(category_a_suggestion)

    def test_03_verify_category_a_1(self):
        self.driver.get("http://localhost:3000/category-a-1")
        self.assertTrue("Category A-1" in self.driver.title)
        category_a_1 = self.driver.find_element_by_name("category-a-1")
        self.assertIsNotNone(category_a_1)

    def test_04_verify_button(self):
        self.driver.get("http://localhost:3000/category-a-1")
        learn_more_button = self.driver.find_element_by_name("Learn more")
        self.assertIsNotNone(learn_more_button)
        learn_more_button.click()
        WebDriverWait(self.driver, 20).until_not(EC.staleElementException)

if __name__ == "__main__":
    unittest.main()