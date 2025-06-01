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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # Accept cookies if present
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        product_elements_tables = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tab-content']//div[@aria-selected='true' and text()='Tables']/ancestor::div[@class='product-tab-list pt-30 pb-55 text-center nav nav-pills']//following-sibling::div[@class='tab-content']/div[@class='fade tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
        )

        if not product_elements_tables:
            self.fail("No products displayed after filtering by Tables.")

        tables_product_count = len(product_elements_tables)

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        product_elements_chairs = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tab-content']//div[@aria-selected='true' and text()='Chairs']/ancestor::div[@class='product-tab-list pt-30 pb-55 text-center nav nav-pills']//following-sibling::div[@class='tab-content']/div[@class='fade tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
        )

        if not product_elements_chairs:
            self.fail("No products displayed after filtering by Chairs.")

        chairs_product_count = len(product_elements_chairs)

        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering by Chairs.")

        # 6. Click "All" to remove the filter.
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        product_elements_all = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tab-content']//div[@aria-selected='true' and text()='All']/ancestor::div[@class='product-tab-list pt-30 pb-55 text-center nav nav-pills']//following-sibling::div[@class='tab-content']/div[@class='fade tab-pane active show']//div[@class='product-wrap-2 mb-25']"))
        )

        if not product_elements_all:
            self.fail("No products displayed after clicking All tab.")

        all_product_count = len(product_elements_all)

        self.assertNotEqual(chairs_product_count, all_product_count, "Product count did not change after clicking All tab.")


if __name__ == "__main__":
    unittest.main()