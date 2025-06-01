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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Tables' tab: {e}")

        # 3. Wait for product grid to update.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']"))
        )

        # 4. Store number of visible products (1 product).
        table_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
        tables_count = len(table_products)
        self.assertTrue(tables_count > 0, "No products displayed after applying 'Tables' filter")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh (3 products).
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Chairs' tab: {e}")

        # Wait for product grid to update.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']"))
        )

        # 6. Verify that the list of products is updated and different from the previous.
        chair_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
        chairs_count = len(chair_products)
        self.assertTrue(chairs_count > 0, "No products displayed after applying 'Chairs' filter")
        self.assertNotEqual(tables_count, chairs_count, "Product count did not change after switching to 'Chairs' filter")

        # 7. Then click the "All" filter to reset (4 products).
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'All' tab: {e}")

        # Wait for product grid to update.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']"))
        )

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
        all_count = len(all_products)
        self.assertTrue(all_count > 0, "No products displayed after applying 'All' filter")
        self.assertTrue(all_count > tables_count, "Product count did not increase after switching to 'All' filter from 'Tables'")
        self.assertTrue(all_count > chairs_count, "Product count did not increase after switching to 'All' filter from 'Chairs'")

if __name__ == "__main__":
    unittest.main()