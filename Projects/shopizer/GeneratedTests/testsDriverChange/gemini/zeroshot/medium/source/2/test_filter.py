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

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        return len(product_elements)

    def test_product_filter(self):
        # 1. Open the home page.
        # Implicitly done in setUp

        # Accept cookies
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_product_count = self.get_product_count()
        if initial_product_count == 0:
            self.fail("Initial product count is 0. Something is wrong with the page.")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        tables_product_count = self.get_product_count()
        if tables_product_count == 0:
            self.fail("No products displayed after filtering by 'Tables'.")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        chairs_product_count = self.get_product_count()
        if chairs_product_count == 0:
            self.fail("No products displayed after filtering by 'Chairs'.")

        if chairs_product_count == tables_product_count:
            self.fail("Product list was not updated after filtering by 'Chairs'.")

        # 6. Click "All" to remove the filter.
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        all_product_count = self.get_product_count()

        if all_product_count == 0:
            self.fail("No products displayed after clicking 'All'.")

        self.assertNotEqual(chairs_product_count, all_product_count, "Product count did not change after clicking All")
        self.assertEqual(initial_product_count, all_product_count, "All product count is not equal to initial product count")

if __name__ == "__main__":
    unittest.main()