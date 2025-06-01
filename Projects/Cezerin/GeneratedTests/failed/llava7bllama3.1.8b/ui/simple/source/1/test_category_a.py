from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebpageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')

    def test_homepage_ui(self):
        # Check that main UI components are present
        self._check_component_visible_by_id('header', 'Header is not visible')
        self._check_component_visible_by_class('nav-link', 'Navigation links are not visible')
        self._check_component_visible_by_class('product-card', 'Product cards are not visible')
        self._check_component_visible_by_id('footer', 'Footer is not visible')

    def test_category_a_ui(self):
        # Click on category a link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Category A']"))).click()
        
        # Check that main UI components are present
        self._check_component_visible_by_id('header', 'Header is not visible')
        self._check_component_visible_by_class('nav-link', 'Navigation links are not visible')
        self._check_component_visible_by_class('product-card', 'Product cards are not visible')
        self._check_component_visible_by_id('footer', 'Footer is not visible')

    def test_category_a_1_ui(self):
        # Click on category a-1 link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Category A - 1']"))).click()
        
        # Check that main UI components are present
        self._check_component_visible_by_id('header', 'Header is not visible')
        self._check_component_visible_by_class('nav-link', 'Navigation links are not visible')
        self._check_component_visible_by_class('product-card', 'Product cards are not visible')
        self._check_component_visible_by_id('footer', 'Footer is not visible')

    def _check_component_visible_by_id(self, component_id, error_message):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, component_id)))
        except TimeoutException:
            self.fail(error_message)

    def _check_component_visible_by_class(self, component_class, error_message):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, component_class)))
        except TimeoutException:
            self.fail(error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()