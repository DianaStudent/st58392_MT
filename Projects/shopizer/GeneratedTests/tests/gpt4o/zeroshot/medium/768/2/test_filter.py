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

    def test_product_filter(self):
        driver = self.driver

        # Check that home page is loaded
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.section-title-5')))
        except:
            self.fail("Home page did not load properly")

        # Click on the "Tables" tab
        tables_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']/h4")))
        tables_tab.click()

        # Verify that at least one product appears
        try:
            products_tables = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-wrap-2')))
            self.assertTrue(len(products_tables) > 0, "No products found for tables filter")
        except:
            self.fail("Failed to load products in tables filter")

        # Click on the "Chairs" tab
        chairs_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']/h4")))
        chairs_tab.click()

        # Verify that product list is updated
        try:
            products_chairs = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-wrap-2')))
            self.assertTrue(len(products_chairs) > 0, "No products found for chairs filter")
        except:
            self.fail("Failed to load products in chairs filter")

        # Click on "All" to remove the filter
        all_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']/h4")))
        all_tab.click()

        # Verify that the full list of products is shown
        try:
            products_all = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-wrap-2')))
            self.assertTrue(len(products_all) > len(products_chairs), "Product list did not reset to show all products")
        except:
            self.fail("Failed to load products in all filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()