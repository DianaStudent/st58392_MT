import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_filter_tables(self):
        # Click on the 'Tables' filter
        try:
            filter_tables = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-rb-event-key='tables']")))
            filter_tables.click()
        except:
            self.fail("Tables filter tab not found or not clickable.")

        # Verify at least one product is displayed after filter
        try:
            products_after_filter = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
            self.assertGreater(len(products_after_filter), 0, "No products displayed after applying tables filter.")
        except:
            self.fail("Failed to find products after applying tables filter.")

    def test_filter_chairs(self):
        # Click on the 'Chairs' filter
        try:
            filter_chairs = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-rb-event-key='chairs']")))
            filter_chairs.click()
        except:
            self.fail("Chairs filter tab not found or not clickable.")

        # Verify at least one product is displayed after filter
        try:
            products_after_filter = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
            self.assertGreater(len(products_after_filter), 0, "No products displayed after applying chairs filter.")
        except:
            self.fail("Failed to find products after applying chairs filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()