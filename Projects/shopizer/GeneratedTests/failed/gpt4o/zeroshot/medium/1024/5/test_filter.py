from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify the homepage is loaded
        try:
            homepage_header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Home page not loaded properly")

        # Accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass

        # Click on the "Tables" tab to filter products
        tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4='Tables']")))
        tables_tab.click()

        # Verify that at least one product appears for Tables
        try:
            tables_products = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div[contains(@class, 'product-wrap-2')]"))
            )
            if not tables_products:
                self.fail("No products found for Tables filter")
        except:
            self.fail("No products found for Tables filter")

        tables_count = len(tables_products)

        # Click on the "Chairs" tab to change the filter
        chairs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4='Chairs']")))
        chairs_tab.click()

        # Verify that product list is updated for Chairs
        try:
            chairs_products = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div[contains(@class, 'product-wrap-2')]"))
            )
            if not chairs_products:
                self.fail("No products found for Chairs filter")
        except:
            self.fail("No products found for Chairs filter")

        chairs_count = len(chairs_products)
        self.assertNotEqual(tables_count, chairs_count, "Product count did not change after filter change")

        # Click "All" to remove the filter
        all_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4='All']")))
        all_tab.click()

        # Confirm that the full list of products is shown
        try:
            all_products = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div[contains(@class, 'product-wrap-2')]"))
            )
            if not all_products:
                self.fail("No products found for All filter")
        except:
            self.fail("No products found for All filter")

        all_count = len(all_products)
        self.assertGreaterEqual(all_count, max(tables_count, chairs_count), "Full product list not shown")

if __name__ == "__main__":
    unittest.main()