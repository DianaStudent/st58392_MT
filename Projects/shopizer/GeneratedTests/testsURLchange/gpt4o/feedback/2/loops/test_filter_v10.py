import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        driver.get('http://localhost/')

        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            self.fail("Cookie accept button not found or clickable.")

        # Click on "Tables" filter
        tables_filter = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='tables']")))
        tables_filter.click()

        # Wait for the "Tables" product grid to update
        products_after_tables_filter = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2")))
        self.assertTrue(len(products_after_tables_filter) == 1, "Tables filter did not display the correct number of products.")

        # Click on "Chairs" filter
        chairs_filter = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='chairs']")))
        chairs_filter.click()

        # Wait for the "Chairs" product grid to update
        products_after_chair_filter = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2")))
        self.assertTrue(len(products_after_chair_filter) == 3, "Chairs filter did not display the correct number of products.")
        
        # Click on "All" filter
        all_filter = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='all']")))
        all_filter.click()

        # Wait for the "All" product grid to update
        products_after_all_filter = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2")))
        self.assertTrue(len(products_after_all_filter) == 4, "All filter did not display the correct number of products.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()