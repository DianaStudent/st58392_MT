import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual URL
        self.search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-input")))
        self.filter_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-button")))

    def test_product_search_and_filter(self):
        # Perform product search
        self.search_input.send_keys("book")
        self.search_input.submit()

        # Apply price filter by navigating to a URL that includes the price parameter
        self.driver.get("http://max/")  # Replace with the actual URL

        # Confirm success by checking that the resulting product grid is updated
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#product-grid")))
        product_grid = self.driver.find_element(By.CSS_SELECTOR, "#product-grid")
        self.assertEqual(len(product_grid.find_elements(By.TAG_NAME, "li")), 4)  # Replace with the actual number of products

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()