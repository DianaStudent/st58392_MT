import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://max/')

    def test_search_filter_price_range(self):
        # Step 1: Open the home page.
        self.driver.get('http://max/')

        # Step 2: Click on the "Search" link.
        search_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Search'))
        )
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'search-field'))
        )
        search_field.send_keys('book')
        search_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'submit-search'))
        )
        search_submit_button.click()

        # Step 4: Wait for the search results to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-results'))
        )

        # Step 5: Locate and interact with the price range slider:
        price_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#price-slider .range-handle'))
        )
        # Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        price_slider.click()
        price_slider.send_keys('0')
        self.driver.execute_script("arguments[0].scrollIntoView(false);", price_slider)

        # Step 6: Wait for the filtering to apply dynamically.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-grid'))
        )

        # Confirm that:
        self.assertEqual(len(self.driver.find_elements_by_css_selector('.product-grid')), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()