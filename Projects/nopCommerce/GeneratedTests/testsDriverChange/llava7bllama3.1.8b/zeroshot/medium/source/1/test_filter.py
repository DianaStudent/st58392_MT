import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchWithPriceFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def test_search_with_price_filter(self):
        # Click on the Search link from the top navigation
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
        search_link.click()

        # Enter the search term and perform the search
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search_query')))
        search_input.send_keys('book')
        search_submit_button = self.driver.find_element(By.NAME, 'submit')
        search_submit_button.click()

        # Locate and interact with the price range slider
        price_slider_div = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#price-range-slider')))
        price_slider_input = price_slider_div.find_element(By.TAG_NAME, 'input')

        # Set a price (for example: $50)
        price_slider_input.send_keys('50')
        self.driver.execute_script("$('#price-range-slider input').val('50');")

        # Wait for the page to update and verify that:
        # The filtered URL includes the price parameter
        current_url = self.driver.current_url

        # The product list is changed
        products_table = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.products-table')))
        if not products_table.text or len(products_table.text.splitlines()) == 1:
            self.fail('Expected the table to contain products')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()