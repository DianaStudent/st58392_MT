import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

        # Accept cookies if the banner is present
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass  # No cookie banner

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Tables' tab: {e}")

        # 3. Wait for product grid to update.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']//a[@href='/product/olive-table']"))
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Tables': {e}")

        # 4. Store number of visible products.
        products_tables = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        num_products_tables = len(products_tables)
        if num_products_tables == 0:
            self.fail("No products displayed after filtering by 'Tables'")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Chairs' tab: {e}")

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']//a[@href='/product/chair']"))
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Chairs': {e}")

        # 6. Verify that the list of products is updated and different from the previous.
        products_chairs = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        num_products_chairs = len(products_chairs)

        if num_products_chairs == 0:
            self.fail("No products displayed after filtering by 'Chairs'")

        self.assertNotEqual(num_products_tables, num_products_chairs, "Product count did not change after filtering by 'Chairs'")

        # 7. Then click the "All" filter to reset.
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'All' tab: {e}")

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']//a[@href='/product/chair']"))
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'All': {e}")

        # 8. Confirm that product list contains more items than after previous filters.
        products_all = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        num_products_all = len(products_all)

        if num_products_all == 0:
            self.fail("No products displayed after filtering by 'All'")

        self.assertGreater(num_products_all, num_products_tables, "Product count is not greater after filtering by 'All'")
        self.assertGreater(num_products_all, num_products_chairs, "Product count is not greater after filtering by 'All'")

if __name__ == "__main__":
    unittest.main()