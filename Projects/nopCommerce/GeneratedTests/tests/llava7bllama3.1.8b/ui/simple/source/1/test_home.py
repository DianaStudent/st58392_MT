import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMax(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/')

    def test_main_ui_components_are_present(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'header'))
        )
        self.assertIsNotNone(header)
        
        # Search bar
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search-bar'))
        )
        self.assertIsNotNone(search_bar)
        
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav ul li a'))
        )
        self.assertGreaterEqual(len(navigation_links), 1)
        
        # Product listing
        product_listing = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-listing'))
        )
        self.assertIsNotNone(product_listing)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()