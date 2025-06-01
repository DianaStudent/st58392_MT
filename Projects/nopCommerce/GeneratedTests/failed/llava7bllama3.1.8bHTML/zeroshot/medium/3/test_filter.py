from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestPriceFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        
    def test_price_filter(self):
        # Click on the "Search" link from the top navigation.
        search_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search')]"))
        )
        search_link.click()
        
        # Enter the search term and perform the search.
        search_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-box"))
        )
        search_box.send_keys("book")
        search_box.submit()
        
        # Locate and interact with the price range slider.
        price_slider = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='price-slider']"))
        )
        price_slider.click()
        
        # Wait for the page to update and verify that:
        #   - The filtered URL includes the price parameter.
        self.assertIn("price=1-100", self.driver.current_url)
        
        #   - The product list is changed
        updated_product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid-item']"))
        )
        self.assertGreater(len(updated_product_list), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()