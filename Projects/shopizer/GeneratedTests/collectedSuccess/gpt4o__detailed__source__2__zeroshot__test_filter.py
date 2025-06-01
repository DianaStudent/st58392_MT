import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if the consent button is present
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if accept_button:
                accept_button.click()
        except Exception:
            self.fail("Cookie consent button couldn't be located.")

        # Click on the "Tables" filter tab
        tables_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-rb-event-key="tables"]')))
        tables_tab.click()

        # Wait for product grid to update and verify one product is displayed
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')))
        tables_products = driver.find_elements(By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')
        self.assertEqual(len(tables_products), 1)

        # Switch to the "Chairs" filter tab
        chairs_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-rb-event-key="chairs"]')))
        chairs_tab.click()

        # Wait for product grid to update and verify three products are displayed
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')))
        chairs_products = driver.find_elements(By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')
        self.assertEqual(len(chairs_products), 3)

        # Assert that the list of products is updated and different from the previous
        self.assertNotEqual(tables_products, chairs_products)

        # Click on the "All" filter tab
        all_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-rb-event-key="all"]')))
        all_tab.click()

        # Wait for product grid to update and verify more products are displayed than previous filters
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')))
        all_products = driver.find_elements(By.CSS_SELECTOR, '.tab-pane.active.show .product-wrap-2')
        self.assertEqual(len(all_products), 4)
        self.assertGreater(len(all_products), len(chairs_products))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()