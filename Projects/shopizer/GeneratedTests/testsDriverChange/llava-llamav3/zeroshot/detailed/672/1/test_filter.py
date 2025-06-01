import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.locator import LocatorElement

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20, time=1)

    def tearDown(self):
        self.driver.quit()

    def test_filter_tables_and_chairs(self):
        # Apply the "Tables" filter
        tables_filter = WebDriverWait(self.driver, 20).until(
            SelectorElement(By.XPATH, "//a[@href='tables']"))
        tables_filter.click()
        
        # Store number of visible products after applying the "Tables" filter
        self.assertEqual(len(self.driver.find_elements_by_xpath("//div[@class='product']")), 1)
        self.assertTrue("Tables" in self.driver.title)

        # Apply the "Chairs" filter and wait for grid to refresh
        chairs_filter = WebDriverWait(self.driver, 20).until(
            SelectorElement(By.XPATH, "//a[@href='chairs']"))
        chairs_filter.click()
        
        # Store number of visible products after applying the "Chairs" filter
        self.assertEqual(len(self.driver.find_elements_by_xpath("//div[@class='product']")), 3)
        self.assertTrue("All" in self.driver.title)

    def test_filter_all(self):
        all_filter = WebDriverWait(self.driver, 20).until(
            SelectorElement(By.XPATH, "//a[@href='all']"))
        all_filter.click()
        
        # Confirm that product list contains more items than after previous filters
        self.assertEqual(len(self.driver.find_elements_by_xpath("//div[@class='product']")), 4)
        self.assertTrue("All" in self.driver.title)

if __name__ == "__main__":
    unittest.main()