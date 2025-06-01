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

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Tables" tab to filter products.
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Failed to click 'Tables' tab: {e}")

        # 3. Verify that at least one product appears.
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
            )
            product_elements_tables = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")

            if not product_elements_tables:
                self.fail("No products displayed after filtering by 'Tables'")
            initial_product_count = len(product_elements_tables)
            if initial_product_count == 0:
                self.fail("No products displayed after filtering by 'Tables'")
        except Exception as e:
            self.fail(f"Failed to verify products after filtering by 'Tables': {e}")

        # 4. Click on the "Chairs" tab to change the filter.
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Failed to click 'Chairs' tab: {e}")

        # 5. Verify that product list is updated.
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
            )
            product_elements_chairs = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")

            if not product_elements_chairs:
                self.fail("No products displayed after filtering by 'Chairs'")

            new_product_count = len(product_elements_chairs)
            if new_product_count == 0:
                self.fail("No products displayed after filtering by 'Chairs'")

            if initial_product_count == new_product_count:
                self.fail("Product count did not change after filtering by 'Chairs'")
        except Exception as e:
            self.fail(f"Failed to verify products after filtering by 'Chairs': {e}")

        # 6. Click "All" to remove the filter.
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Failed to click 'All' tab: {e}")

        # 7. Confirm that the full list of products is shown.
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
            )
            product_elements_all = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")

            if not product_elements_all:
                self.fail("No products displayed after filtering by 'All'")

            all_product_count = len(product_elements_all)
            if all_product_count == 0:
                self.fail("No products displayed after filtering by 'All'")

            if new_product_count == all_product_count:
                self.fail("Product count did not change after filtering by 'All'")

        except Exception as e:
            self.fail(f"Failed to verify products after filtering by 'All': {e}")


if __name__ == "__main__":
    unittest.main()