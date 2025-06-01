import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a")
        
    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for the header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertIsNotNone(header, "Header is not present")

        # Wait for the search input
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-input"))
        )
        self.assertIsNotNone(search_input, "Search input is not present")
        
        # Verify products are visible
        product_a = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Product A"))
        )
        product_b = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Product B"))
        )
        self.assertIsNotNone(product_a, "Product A is not visible")
        self.assertIsNotNone(product_b, "Product B is not visible")
        
        # Verify the filter button is visible
        filter_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Filter products']"))
        )
        self.assertIsNotNone(filter_button, "Filter button is not present")
        
        # Verify footer is visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "footer"))
        )
        self.assertIsNotNone(footer, "Footer is not present")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()