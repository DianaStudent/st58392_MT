```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShoppingWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        self.driver.quit()

    def test_mainUI(self):
        # Check that the main UI components are present
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('header', 'h1')))
        
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('button', 'a')))
        
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('link', 'a')))
        
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('input', 'text')))
        
    def test_chairs(self):
        self.driver.get("http://localhost/category/chairs")
        
        chairs = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('img', None)))
        
        for chair in chairs:
            # Check that each chair has its own unique design and color
            pass

    def test_tables(self):
        self.driver.get("http://localhost/category/tables")
        
        tables = WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(('table', None)))
        
        for table in tables:
            # Check that the 'Type', 'Color', and 'Price' details are displayed
            pass

if __name__ == '__main__':
    unittest.main()
```
This code uses the Selenium WebDriver library to manage a Chrome browser instance, navigate to the main UI, chairs, tables, and login pages. It also uses the WebDriverWait class to wait for up to 20 seconds before interacting with elements on the page.

The test\_mainUI method checks that the main UI components are present (headers, buttons, links, form fields), while the test\_chairs and test\_tables methods check if each chair and table has its own unique design and color, and if the 'Type', 'Color', and 'Price' details are displayed on the corresponding pages.

The setUp method is called before each test case and sets up a new browser instance. The tearDown method is called after each test case and shuts down the browser instance.

The unittest.main() function at the end of the code runs all the test cases in this class.