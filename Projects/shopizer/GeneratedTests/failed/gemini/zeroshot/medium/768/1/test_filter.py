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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page.
        # Implicitly done in setUp

        # 2. Click on the "Tables" tab to filter products.
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Tables' tab: {e}")

        # 3. Verify that at least one product appears.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
            )
            product_elements = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
            self.assertTrue(len(product_elements) > 0, "No products displayed after filtering by 'Tables'")
            tables_product_count = len(product_elements)
        except Exception as e:
            self.fail(f"Could not verify products after filtering by 'Tables': {e}")

        # 4. Click on the "Chairs" tab to change the filter.
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Chairs' tab: {e}")

        # 5. Verify that product list is updated.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
            )
            product_elements = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
            self.assertTrue(len(product_elements) > 0, "No products displayed after filtering by 'Chairs'")
            chairs_product_count = len(product_elements)
            self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering by 'Chairs'")
        except Exception as e:
            self.fail(f"Could not verify products after filtering by 'Chairs': {e}")

        # 6. Click "All" to remove the filter.
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'All' tab: {e}")

        # 7. Confirm that the full list of products is shown.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
            )
            product_elements = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
            self.assertTrue(len(product_elements) > 0, "No products displayed after clicking 'All'")
            all_product_count = len(product_elements)
            self.assertNotEqual(chairs_product_count, all_product_count, "Product count did not change after clicking 'All'")
        except Exception as e:
            self.fail(f"Could not verify products after clicking 'All': {e}")


if __name__ == "__main__":
    unittest.main()