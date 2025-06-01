from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestFilteringProcess(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_filtering_process(self):
        # Step 1: Search for the product with query "book"
        search_box = self.driver.find_element_by_name("searchbox")
        search_box.send_keys("book")
        time.sleep(2)

        # Step 2: Select a filter
        filters_list = self.driver.find_elements_by_css_selector(".filter-list")
        filter_list_text = [f.text for f in filters_list]
        if "Price" not in filter_list_text:
            print("Filter 'Price' is missing. Test failed.")
            self.fail()

        filter_select = Select(self.driver.find_element_by_name("filter"))
        time.sleep(1)

        # Step 3: Select a specific price range
        price_range = self.driver.find_element_by_name("price")
        if len(price_range.get_attribute("options")) <= 0:
            print("No options available. Test failed.")
            self.fail()

        time.sleep(2)

        # Step 4: Confirm success by checking the resulting product grid
        product_grid = self.driver.find_element_by_css_selector(".product-grid")
        self.assertTrue(product_grid, "Product grid is empty.")

if __name__ == '__main__':
    unittest.main()