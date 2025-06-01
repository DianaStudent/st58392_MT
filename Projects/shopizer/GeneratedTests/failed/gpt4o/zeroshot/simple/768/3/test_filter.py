from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_filter_products(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies if the dialog is present
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except Exception:
            self.fail("Cookies acceptance button not found or clickable.")

        # Wait for and count initial products displayed
        initial_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrap-2']")))
        initial_product_count = len(initial_products)
        
        if initial_product_count == 0:
            self.fail("No initial products found.")

        # Click the "Tables" filter tab
        try:
            tables_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']")))
            tables_filter.click()
        except Exception:
            self.fail("Tables filter tab not found or clickable.")

        # Wait for products to refresh and count them
        filtered_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrap-2']")))
        filtered_product_count = len(filtered_products)

        if filtered_product_count == 0:
            self.fail("No products found after applying table filter.")
        
        # Assert product count changes
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()