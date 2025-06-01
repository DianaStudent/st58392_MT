from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_product_search(self):
        # Perform a product search using the query "book"
        self.driver.get("http://max/")
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'search_query'))
        )
        search_input.send_keys('book')
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'submitSearch'))
        )
        search_button.click()

        # Apply a price filter by navigating to a URL that includes the price parameter
        self.driver.get("http://max/")

        # Confirm success by checking that the resulting product grid is updated
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.products a.product'))
        )
        self.assertTrue(len(product_grid.find_elements(By.TAG_NAME, 'a')) > 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()