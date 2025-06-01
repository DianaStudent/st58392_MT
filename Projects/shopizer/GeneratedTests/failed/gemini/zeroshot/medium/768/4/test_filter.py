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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # Accept cookies
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 1. Open the home page.
        # Implicitly done in setUp

        # Get initial product count
        initial_products = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("Initial product count is zero.")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        tables_products = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        tables_product_count = len(tables_products)
        if tables_product_count == 0:
            self.fail("No products displayed after filtering by Tables.")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        chairs_products = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        chairs_product_count = len(chairs_products)
        if chairs_product_count == 0:
            self.fail("No products displayed after filtering by Chairs.")

        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering.")

        # 6. Click "All" to remove the filter.
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        all_products = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        all_product_count = len(all_products)
        if all_product_count == 0:
            self.fail("No products displayed after clicking All tab.")

        self.assertEqual(initial_product_count, all_product_count, "Product count did not return to initial count after removing filter.")


if __name__ == "__main__":
    unittest.main()