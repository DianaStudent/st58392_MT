```
from selenium import webdriver
import unittest
from html_data import filter_detailed

class TestFilterDetailed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_detailed(self):
        # Step 1: Open the home page.
        self.driver.get(filter_detailed['url'])
        
        # Step 2: Apply the "Tables" filter by clicking the corresponding tab.
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(filter_detailed['tables_filter']))

        # Step 3: Wait for product grid to update.
        WebDriverWait(self.driver, 20).until_not(None)

        # Step 4: Store number of visible products (1 product).
        self.assertEqual(len(self.driver.find_elements_by_xpath(filter_detailed['product_grid'])) == 1, "Failed to find at least one product in the grid.")

        # Step 5: Switch to the "Chairs" filter and wait for grid to refresh.
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(filter_detailed['chairs_filter']))

        # Step 6: Verify that the list of products is updated and different from the previous.
        self.assertTrue(len(self.driver.find_elements_by_xpath(filter_detailed['product_grid'])) != len(self.driver.find_elements_by_xpath(filter_detailed['prev_product_grid'])), "Failed to find at least one product in the grid.")

        # Step 7: Then click the "All" filter to reset.
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(filter_detailed['all_filter']))

        # Step 8: Confirm that product list contains more items than after previous filters.
        self.assertTrue(len(self.driver.find_elements_by_xpath(filter_detailed['product_grid'])) > len(self.driver.find_elements_by_xpath(filter_detailed['prev_product_grid'])), "Failed to find at least one product in the grid.")

if __name__ == '__main__':
    unittest.main()
```
Please note that this test code is just an example, and it may not work as intended without proper modification or validation. It is recommended to thoroughly test the code before running it on a production environment to ensure its correctness and reliability.