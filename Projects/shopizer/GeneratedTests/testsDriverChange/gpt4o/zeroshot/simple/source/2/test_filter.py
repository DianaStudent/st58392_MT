import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver

        # Wait for home page to load and check presence of 'Featured Products' section
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-tab-list")))

        # Select 'Tables' filter tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//a[@data-rb-event-key='tables']"
                ))
            )
            tables_tab.click()
        except:
            self.fail("Tables filter tab not found or not clickable.")

        # Check that at least one product is displayed for tables
        try:
            filtered_products = self.wait.until(EC.presence_of_all_elements_located((
                By.CLASS_NAME, "product-wrap-2"
            )))
            if not filtered_products:
                self.fail("No products displayed after filtering by tables.")
        except:
            self.fail("Failed to locate products after filtering by tables.")

        # Select 'Chairs' filter tab
        try:
            chairs_tab = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//a[@data-rb-event-key='chairs']"
                ))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs filter tab not found or not clickable.")

        # Check that at least one product is displayed for chairs
        try:
            filtered_products = self.wait.until(EC.presence_of_all_elements_located((
                By.CLASS_NAME, "product-wrap-2"
            )))
            if not filtered_products:
                self.fail("No products displayed after filtering by chairs.")
        except:
            self.fail("Failed to locate products after filtering by chairs.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()