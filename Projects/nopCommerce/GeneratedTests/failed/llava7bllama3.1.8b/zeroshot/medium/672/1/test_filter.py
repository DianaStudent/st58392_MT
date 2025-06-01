from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerce(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        
    def tearDown(self):
        self.driver.quit()

    def test_search_product(self):
        # Open the search page
        self.driver.find_element(By.LINK_TEXT, 'Search').click()
        
        # Enter the search term and perform the search
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'q')))
        search_input.send_keys('book')
        search_input.submit()

        # Locate and interact with the price range slider
        price_slider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#price-slider')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", price_slider)
        price_slider.send_keys('10-50')

        # Wait for the page to update and verify that
        # - The filtered URL includes the price parameter.
        current_url = self.driver.current_url
        self.assertTrue(current_url.__contains__('price=10-50'))

        # - The product list is changed
        products = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-grid > li')))
        self.assertGreater(len(products), 0)

if __name__ == '__main__':
    unittest.main()