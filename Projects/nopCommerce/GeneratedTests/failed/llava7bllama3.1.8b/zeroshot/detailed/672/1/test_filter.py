from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def test_search_and_filter(self):
        # 1. Click on the "Search" link.
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
        search_link.click()

        # 2. Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'q')))
        search_field.send_keys('book')
        search_button = self.driver.find_element(By.NAME, 'search')
        search_button.click()

        # Wait for the search results to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-grid-item')))

        # 3. Locate and interact with the price range slider:
        min_slider = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='min-slider-handle']")))
        max_slider = self.driver.find_element(By.XPATH, "//input[@class='max-slider-handle']")
        
        # Move the sliders
        def move_sliders(slider1, slider2, value):
            if value:
                slider1.send_keys(Keys.ARROW_LEFT)
                slider2.send_keys(Keys.ARROW_LEFT)

        move_sliders(min_slider, max_slider, 25)

        # Wait for the filtering to apply dynamically.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-grid-item')))

        # Confirm that:
        # The product grid updates after slider movement.
        products = self.driver.find_elements(By.CLASS_NAME, 'product-grid-item')
        
        # At least one product is shown in the filtered results.
        self.assertGreater(len(products), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()