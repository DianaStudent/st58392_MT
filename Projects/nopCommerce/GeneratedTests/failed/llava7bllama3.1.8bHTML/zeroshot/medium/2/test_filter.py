from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_product_search(self):
        # Click on the "Search" link from the top navigation.
        search_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Search']"))
        )
        search_link.click()

        # Enter the search term and perform the search.
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search-input"))  # Change id according to your HTML
        )
        search_input.send_keys("book")
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
        )
        search_button.click()

        # Locate and interact with the price range slider.
        price_slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "price-slider"))  # Change id according to your HTML
        )
        price_slider.send_keys("25")

        # Wait for the page to update and verify that:
        # The filtered URL includes the price parameter.
        current_url = self.driver.current_url
        self.assertIn("price=25", current_url)

        # The product list is changed
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Book5']"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()