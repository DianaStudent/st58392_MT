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

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        """Counts the number of product items displayed."""
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        return len(product_elements)

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_product_count = self.get_product_count()
        self.assertGreater(initial_product_count, 0, "Initial product count should be greater than 0")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        tables_product_count = self.get_product_count()
        self.assertGreater(tables_product_count, 0, "Tables product count should be greater than 0")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        chairs_product_count = self.get_product_count()
        self.assertGreater(chairs_product_count, 0, "Chairs product count should be greater than 0")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count should change after filtering")

        # 6. Click "All" to remove the filter.
        all_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        all_product_count = self.get_product_count()
        self.assertEqual(all_product_count, initial_product_count, "All product count should be equal to initial product count")

if __name__ == "__main__":
    unittest.main()