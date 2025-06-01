from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPriceFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_price_filter(self):
        # Open the homepage
        self.driver.get("http://max/")

        # Click on the "Search" link from the top navigation
        search_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search')]")))
        search_link.click()

        # Enter the search term and perform the search
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search_term")))
        search_input.send_keys("book")
        search_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@name='search_form']")))
        search_form.submit()

        # Locate and interact with the price range slider
        price_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "price-slider")))
        price_slider.click()

        # Wait for the page to update and verify that:
        # The filtered URL includes the price parameter.
        current_url = self.driver.current_url
        self.assertIn("price=100", current_url)

        # The product list is changed
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']")))
        initial_products = len(product_grid.find_elements(By.TAG_NAME, "li"))
        time.sleep(1)  # wait for the page to update
        final_products = len(product_grid.find_elements(By.TAG_NAME, "li"))

        self.assertNotEqual(initial_products, final_products)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()