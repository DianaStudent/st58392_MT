from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

        try:
            cookie_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found")

        # 3. Wait for product grid to update.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/olive-table']/img"))
            )
        except:
            self.fail("Tables products not loaded")

        # 4. Store number of visible products.
        tables_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[@class='product-wrap-2 mb-25']")
        tables_count = len(tables_products)
        self.assertTrue(tables_count > 0, "No tables products found")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        try:
            chairs_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/chair']/img"))
            )
        except:
            self.fail("Chairs products not loaded")

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[@class='product-wrap-2 mb-25']")
        chairs_count = len(chairs_products)
        self.assertTrue(chairs_count > 0, "No chairs products found")
        self.assertNotEqual(tables_count, chairs_count, "Product count did not change after filtering")

        # 7. Then click the "All" filter to reset.
        try:
            all_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except:
            self.fail("All tab not found")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/olive-table']/img"))
            )
        except:
            self.fail("All products not loaded")

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[@class='product-wrap-2 mb-25']")
        all_count = len(all_products)
        self.assertTrue(all_count > 0, "No All products found")
        self.assertTrue(all_count > tables_count and all_count > chairs_count, "All product count not greater than previous filters")

if __name__ == "__main__":
    unittest.main()