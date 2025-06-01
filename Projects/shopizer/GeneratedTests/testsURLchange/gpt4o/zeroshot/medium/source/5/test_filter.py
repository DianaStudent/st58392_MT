import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filters(self):
        driver = self.driver

        # Close cookie consent if it exists
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            pass  # Cookie consent not present, continue

        # Select "Tables" filter tab
        tables_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Tables']]")))
        tables_tab.click()

        # Verify that at least one table product is visible
        table_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/product/') and img]")))
        if not table_products:
            self.fail("No products displayed under 'Tables' filter.")

        # Click on the "Chairs" filter tab
        chairs_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Chairs']]")))
        chairs_tab.click()

        # Verify that the chair product list is updated
        chair_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/product/') and img]")))
        if not chair_products:
            self.fail("No products displayed under 'Chairs' filter.")
        if len(chair_products) == len(table_products):
            self.fail("Product count did not change after selecting 'Chairs' filter.")

        # Click on the "All" filter tab
        all_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='All']]")))
        all_tab.click()

        # Verify that the full list of products is displayed
        all_products = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/product/') and img]")))
        if not all_products:
            self.fail("No products displayed under 'All' filter.")
        if len(all_products) <= len(table_products) or len(all_products) <= len(chair_products):
            self.fail("Product count is not restored to full list after removing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()