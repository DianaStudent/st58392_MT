import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Find search box
        try:
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
            search_button = driver.find_element(By.CLASS_NAME, 'search-box-button')
        except Exception as e:
            self.fail(f'Search elements are missing: {e}')
        
        # Perform search
        search_box.send_keys('book')
        search_button.click()

        # Check if search page is loaded
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results')))
        except Exception as e:
            self.fail(f'Search results page did not load: {e}')

        # Apply price filter by navigating to the URL with filter parameters
        driver.get('http://max/search?advs=false&q=book&fromPrice=15&toPrice=50')

        # Verify updated product grid
        try:
            self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.product-item')))
        except Exception as e:
            self.fail(f'Product grid did not update with price filter: {e}')
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()