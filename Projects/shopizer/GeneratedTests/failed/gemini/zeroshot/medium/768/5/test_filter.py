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

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 1. Open the home page.
        # No explicit action needed, already done in setUp

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_count = len(initial_products)
        self.assertGreater(initial_count, 0, "Initial product count should be greater than 0")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        tables_products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        tables_count = len(tables_products)
        self.assertGreater(tables_count, 0, "Tables product count should be greater than 0")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        chairs_products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        chairs_count = len(chairs_products)
        self.assertGreater(chairs_count, 0, "Chairs product count should be greater than 0")
        self.assertNotEqual(tables_count, chairs_count, "Product count should change after filtering")

        # 6. Click "All" to remove the filter.
        all_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        all_products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        all_count = len(all_products)
        self.assertEqual(initial_count, all_count, "All product count should be equal to initial product count")

if __name__ == "__main__":
    unittest.main()