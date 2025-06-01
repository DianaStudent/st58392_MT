from selenium import webdriver
import unittest
from unittest.mock import MagicMock
import time
from selenium.webdriver.common.keys import Keys

class TestShopPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Check that the main UI components are present and visible
        assert "header" in driver.page_source, "Header not found"
        assert "body" in driver.page_source, "Body not found"
    
    def test_click_chairs_link(self):
        driver = self.driver
        driver.get("http://localhost/category/chairs")
        
        # Check that the UI reacts visually
        time.sleep(2)
        assert "Tables" in driver.page_source, "Table is missing"
        assert "Chairs" in driver.page_source, "Chair is missing"

if __name__ == "__main__":
    unittest.main()