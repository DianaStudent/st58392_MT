from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_product_search(self):
        # Open the home page
        self.driver.get("http://max/")

        # Click on the "Search" link
        search_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_field.send_keys("book")
        search_field.send_keys(Keys.RETURN)

        # Wait for the search results to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-results"))
        )

        # Locate and interact with the price range slider:
        min_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#price-range > input:nth-child(1)"))
        )
        max_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#price-range > input:nth-child(2)"))
        )

        # Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25)
        min_slider.send_keys(Keys.END)
        max_slider.send_keys(Keys.HOME)

        # Wait for the filtering to apply dynamically
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-results"))
        )

        # Confirm that:
        self.assertIn("Results", self.driver.page_source)
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#search-results > div.product-grid-item"))
        )
        self.assertGreater(len(products), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()