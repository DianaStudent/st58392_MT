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
        except Exception as e:
            self.fail(f"Acceptance button for cookies not found: {str(e)}")

        # Click on "Tables" filter tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Tables filter tab not found: {str(e)}")

        # Wait for product grid to update to 1 product (Olive Table)
        try:
            self.wait.until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-wrap-2")) == 1
            )
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 1, "Incorrect number of products for 'Tables' filter.")
        except Exception as e:
            self.fail(f"Failed to apply 'Tables' filter or incorrect number of products: {str(e)}")

        # Click on "Chairs" filter tab
        try:
            chairs_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Chairs filter tab not found: {str(e)}")

        # Wait for product grid to update to 3 products
        try:
            self.wait.until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-wrap-2")) == 3
            )
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 3, "Incorrect number of products for 'Chairs' filter.")
        except Exception as e:
            self.fail(f"Failed to apply 'Chairs' filter or incorrect number of products: {str(e)}")

        # Click on "All" filter tab
        try:
            all_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"All filter tab not found: {str(e)}")

        # Verify that all products are displayed (4 products)
        try:
            self.wait.until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-wrap-2")) == 4
            )
            products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertEqual(len(products), 4, "Incorrect number of products for 'All' filter.")
        except Exception as e:
            self.fail(f"Failed to apply 'All' filter or incorrect number of products: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()