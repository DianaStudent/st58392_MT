from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        self.driver = driver
    
    def tearDown(self):
        self.driver.quit()

    def test_category_a_1(self):
        self.driver.get('http://localhost:3000/category-a-1')
        elements = ['header', 'button', 'links']
        self.assertTrue([element for element in elements if self.driver.find_element_by_name(element)], f'One or more required UI elements are missing: {elements}')
        
if __name__ == '__main__':
    unittest.main()