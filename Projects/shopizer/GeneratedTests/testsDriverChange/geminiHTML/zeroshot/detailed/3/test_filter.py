import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

        # Accept cookies
        try:
            cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']")))
        tables_tab.click()

        # 3. Wait for product grid to update.
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//a[@href='/product/olive-table']/img")))

        # 4. Store number of visible products.
        table_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
        table_products_count = len(table_products)
        self.assertTrue(table_products_count > 0, "No products displayed after applying 'Tables' filter.")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        chairs_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']")))
        chairs_tab.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//a[@href='/product/chair']/img")))

        # 6. Verify that the list of products is updated and different from the previous.
        chair_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
        chair_products_count = len(chair_products)
        self.assertTrue(chair_products_count > 0, "No products displayed after applying 'Chairs' filter.")
        self.assertNotEqual(table_products_count, chair_products_count, "Product count did not change after switching filters.")

        # 7. Then click the "All" filter to reset.
        all_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']")))
        all_tab.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//a[@href='/product/olive-table']/img")))

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
        all_products_count = len(all_products)
        self.assertTrue(all_products_count > 0, "No products displayed after applying 'All' filter.")
        self.assertTrue(all_products_count > table_products_count, "Product count did not increase after applying 'All' filter.")
        self.assertTrue(all_products_count > chair_products_count, "Product count did not increase after applying 'All' filter.")


if __name__ == "__main__":
    unittest.main()