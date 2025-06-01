import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless if needed
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('http://max/')

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Perform product search
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.clear()
        search_box.send_keys("book")
        
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        search_button.click()

        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Apply price filter by navigating to a URL with price parameter
        driver.get('http://max/search?q=book&priceRange=0-25')

        # Confirm product grid is updated
        try:
            product_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-wrapper")))
            products = product_grid.find_elements(By.CLASS_NAME, "item-box")
            self.assertGreater(len(products), 0, "Product grid is not updated after applying filter")
        except Exception as e:
            self.fail(f"Product grid not found or other error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()