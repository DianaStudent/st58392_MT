import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class SearchPageUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver
        driver.get('http://max/search')

        # Check header elements
        self.assert_element_present_and_visible(By.CLASS_NAME, 'header')
        self.assert_element_present_and_visible(By.CLASS_NAME, 'header-logo')
        self.assert_element_present_and_visible(By.LINK_TEXT, 'Home page')
        self.assert_element_present_and_visible(By.LINK_TEXT, 'New products')

        # Check search box
        self.assert_element_present_and_visible(By.ID, 'small-searchterms')
        search_button = self.assert_element_present_and_visible(By.CLASS_NAME, 'search-box-button')

        # Check product grid
        self.assert_element_present_and_visible(By.CLASS_NAME, 'product-grid')
        self.assert_element_present_and_visible(By.CLASS_NAME, 'product-title')

        # Interact with search button
        search_button.click()
        self.wait.until(EC.url_contains('/search'))

        # Verify no errors in UI
        self.assertNotIn('Error', driver.title, "UI shows error after interaction")

    def assert_element_present_and_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return element
        except Exception:
            self.fail(f'Element with {by} = {value} is not present or not visible.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()