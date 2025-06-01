from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_filter(self):
        # Click on the filter tab.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='nav-menu']//ul//li[1]"))).click()
        
        # Check that at least one product is displayed after applying filters
        products = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-list-grid']//a")))
        self.assertGreater(len(products), 0)
        
    def test_filter_applied(self):
        # Check that at least one product is displayed after applying filters
        products = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-list-grid']//a")))
        self.assertGreater(len(products), 0)

if __name__ == "__main__":
    unittest.main()