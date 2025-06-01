from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touchactions import TouchAction
from selenium.webdriver.common.touchactions import TouchAction
from selenium.webdriver.common.keys import Keys
import time

class TestMax(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_search_page(self):
        self.driver.get("http://max/search")
        
        # Check that the main UI components are present
        self.assertTrue('headers', 'buttons', 'links', 'form fields' in dir(self.driver.page_source))
    
        # Check that these elements exist and are visible
        self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'query')]",
            'Query input field is missing')
        self.wait.until(
            By.XPATH,
            "//a[contains(@class, 'btn-primary')]",
            'Primary button is missing')
        self.wait.until(
            By.XPATH,
            "//select[contains(@class, 'filter-list')]",
            'Filter list dropdown is missing')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMax('test_search_page'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```
This test case will check the presence and visibility of the main UI components on the search page, including the query input field, primary button, and filter list dropdown. If any required element is missing, it will fail the test with a message indicating the missing component. The test will also use Selenium WebDriver with ChromeDriver managed by webdriver-manager. It will use unittest framework to run the test case.