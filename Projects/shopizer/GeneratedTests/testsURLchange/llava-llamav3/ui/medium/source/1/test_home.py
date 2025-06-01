import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import DriverVersion
from webdriver_manager.utils import get_driver
from html_data import main_page

class TestShopierHomePage(unittest.TestCase):
    def setUp(self):
        # Set up a new WebDriver instance using the ChromeDriverManager.
        url = main_page['home']
        driver_version = DriverVersion.CHROME
        manager = ChromeDriverManager(chrome_executable=driver_version)
        self.driver = get_driver(driver_manager=manager, url=url)

    def tearDown(self):
        # Close the WebDriver instance when finished with it.
        self.driver.quit()

    def test_home_page_elements(self):
        # Verify that the main UI components are present and visible.
        for element in main_page['ui_components']:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((element['selector'], element['description'])))
            if not element['description'] == self.driver.find_element_by_css_selector(element['selector']).text.strip():
                self.fail(f"Element '{element['selector']}': {element['description']} is missing or not displayed correctly.")

if __name__ == '__main__':
    unittest.main()
```
Note: The above code tests for the presence of UI components on the main page and verifies that their descriptions match the actual text displayed. It does not test any interactive elements as per the task description.