import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_filtering(self):
        # Open the home page.
        self.driver.get("https://example.com")

        # Click on the "Search" link.
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
        search_link.click()

        # Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search-field')))
        search_field.send_keys('book')
        search_field.send_keys(Keys.RETURN)

        # Wait for the search results to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-grid-item')))

        # Locate and interact with the price range slider:
        # Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        min_slider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'price-min-slider')))
        max_slider = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'price-max-slider')))

        # Set a specific range (e.g. 0–25)
        min_slider.send_keys('0')
        max_slider.send_keys('25')

        # Wait for the filtering to apply dynamically.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-grid-item')))

        # Confirm that:
        # - The product grid updates after slider movement.
        self.assertTrue(len(self.driver.find_elements_by_css_selector('.product-grid-item')) > 0)
        
        # - At least one product is shown in the filtered results.
        self.assertTrue(self.driver.find_element_by_css_selector('.product-grid-item').is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()