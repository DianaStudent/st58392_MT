from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for and check header elements
            header_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".header .header-links a"))
            )
            self.assertGreater(len(header_links), 0)

            # Check if search form is present
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input#small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button"))
            )

            # Check if products are displayed
            product_items = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-grid .item-box"))
            )
            self.assertGreater(len(product_items), 0)

            # Check if filter by price is present
            price_filter_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-filter.price-range-filter .filter-title"))
            )

            # Check if footer is present
            footer_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".footer .footer-upper a"))
            )
            self.assertGreater(len(footer_links), 0)

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()