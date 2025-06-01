from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApplication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_check_main_ui_components(self):
        # Check header exists and is visible
        header_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'header'))
        )
        self.assertIsNotNone(header_element)

        # Check navigation menu items exist
        navigation_items = ['Chairs', 'Tables']
        for item in navigation_items:
            item_element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, item))
            )
            self.assertIsNotNone(item_element)

        # Check search bar exists and is visible
        search_bar_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'search-bar'))
        )
        self.assertIsNotNone(search_bar_element)

    def test_check_chairs_page_ui_components(self):
        self.driver.get('http://localhost/category/chairs')
        
        # Check header exists and is visible
        header_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'header'))
        )
        self.assertIsNotNone(header_element)

        # Check product grid exists
        product_grid_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'product-grid'))
        )
        self.assertIsNotNone(product_grid_element)

        # Check pagination buttons exist
        pagination_buttons = ['Previous', 'Next']
        for button in pagination_buttons:
            button_element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, button))
            )
            self.assertIsNotNone(button_element)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()