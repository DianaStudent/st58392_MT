import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filters(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except:
            self.fail("Acceptance button for cookies not found.")

        # Click on "Tables" filter tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables filter tab not found.")

        # Wait for product grid to update to 1 product (Olive Table)
        try:
            product_list = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 1, "Incorrect number of products for 'Tables' filter.")
        except:
            self.fail("Failed to apply 'Tables' filter or no products found.")

        # Store the product identifier or count
        tables_product_count = len(products)

        # Click on "Chairs" filter tab
        try:
            chairs_tab = driver.find_element(By.CSS_SELECTOR, "[data-rb-event-key='chairs']")
            chairs_tab.click()
        except:
            self.fail("Chairs filter tab not found.")

        # Wait for product grid to update to 3 products
        try:
            self.wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-wrap-2")) != tables_product_count)
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 3, "Incorrect number of products for 'Chairs' filter.")
        except:
            self.fail("Failed to apply 'Chairs' filter or no products found.")

        # Store the product identifier or count
        chairs_product_count = len(products)

        # Click on "All" filter tab
        try:
            all_tab = driver.find_element(By.CSS_SELECTOR, "[data-rb-event-key='all']")
            all_tab.click()
        except:
            self.fail("All filter tab not found.")

        # Verify that all products are displayed (4 products)
        try:
            self.wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-wrap-2")) != chairs_product_count)
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 4, "Incorrect number of products for 'All' filter.")
        except:
            self.fail("Failed to apply 'All' filter or no products found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()