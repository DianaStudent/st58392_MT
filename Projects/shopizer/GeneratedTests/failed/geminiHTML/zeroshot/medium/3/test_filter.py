from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Tables" tab to filter products.
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not click on 'Tables' tab: {e}")

        # 3. Verify that at least one product appears.
        try:
            product_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            product_count_tables = len(product_elements)
            self.assertGreater(product_count_tables, 0, "No products displayed after filtering by 'Tables'")
        except Exception as e:
            self.fail(f"Could not verify products after filtering by 'Tables': {e}")

        # 4. Click on the "Chairs" tab to change the filter.
        try:
            chairs_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not click on 'Chairs' tab: {e}")

        # 5. Verify that product list is updated.
        try:
            product_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            product_count_chairs = len(product_elements)
            self.assertGreater(product_count_chairs, 0, "No products displayed after filtering by 'Chairs'")
            self.assertNotEqual(product_count_tables, product_count_chairs, "Product count should be updated after filtering by 'Chairs'")
        except Exception as e:
            self.fail(f"Could not verify products after filtering by 'Chairs': {e}")

        # 6. Click "All" to remove the filter.
        try:
            all_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not click on 'All' tab: {e}")

        # 7. Confirm that the full list of products is shown.
        try:
            product_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            product_count_all = len(product_elements)
            self.assertGreater(product_count_all, 0, "No products displayed after clicking 'All'")
            self.assertNotEqual(product_count_all, product_count_chairs, "Product count should be updated after clicking 'All'")
        except Exception as e:
            self.fail(f"Could not verify products after clicking 'All': {e}")


if __name__ == "__main__":
    unittest.main()