from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import unittest

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://max/")

    def test_product_search(self):
        # Perform a product search using the query "book"
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
        search_input.send_keys("book")
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "search")))
        search_button.click()

        # Get the URL to apply a price filter
        url = self.driver.current_url

        # Extract the price parameter from the URL
        import re
        price_pattern = r"price=(\d+)"
        match = re.search(price_pattern, url)
        if not match:
            self.fail("Failed to extract price from URL")
        price = int(match.group(1))

        # Navigate to a URL that includes the price parameter
        new_url = f"http://max/?q=book&price={price}"
        self.driver.get(new_url)

        # Confirm success by checking that the resulting product grid is updated
        product_grid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid")))
        self.assertGreater(len(product_grid.find_elements(By.TAG_NAME, "div")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()