from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class FilterDetailedTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_filter_detailed(self):
        # Apply "Tables" filter
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='filter-list']//a[@href='#filter-tables']"))
        )
        self.failUnless(tables_tab.is_enabled())
        tables_tab.click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )

        # Store number of visible products (1 product)
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-grid']//div")), 3)

        # Switch to the "Chairs" filter and wait for grid to refresh
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='filter-list']//a[@href='#filter-chairs']"))
        )
        self.failUnless(chairs_tab.is_enabled())
        chairs_tab.click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )

        # Verify that the list of products is updated and different from the previous
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-grid']//div")), 3)

        # Then click the "All" filter to reset (4 products)
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='filter-list']//a[@href='#filter-all']"))
        )
        self.failUnless(all_tab.is_enabled())
        all_tab.click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )

        # Confirm that product list contains more items than after previous filters
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-grid']//div")), 4)

if __name__ == '__main__':
    unittest.main()