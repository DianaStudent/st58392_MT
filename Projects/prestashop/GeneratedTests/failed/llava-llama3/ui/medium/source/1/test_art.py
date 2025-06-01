from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Key
import unittest
from selenium.webdriver.support.ui import WebDriverWait

class TestEcomWebsite(unittest.TestCase):
    def setUp(self):
        # Set up a new Chrome driver instance and navigate to the website
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
    
    def tearDown(self):
        # Close the driver when we're done
        self.driver.quit()

    def test_ui_elements(self):
        # Check if main UI components are present and visible
        self.assertTrue(self.driver.find_element_by_css_selector('header'))
        self.assertTrue(self.driver.find_element_by_css_selector('.logo'))
        self.assertTrue(self.driver.find_element_by_css_selector('#searchBar'))

        # Confirm the presence of interactive elements: navigation links, inputs, buttons, banners.
        self.assertTrue(self.driver.find_element_by_css_selector('.tab'))
        self.assertTrue(self.driver.find_element_by_css_selector('#profileTab'))
        self.assertTrue(self.driver.find_element_by_css_selector('#shoppingTab'))
        self.assertTrue(self.driver.find_element_by_css_selector('#pizzaTab'))

if __name__ == '__main__':
    unittest.main()