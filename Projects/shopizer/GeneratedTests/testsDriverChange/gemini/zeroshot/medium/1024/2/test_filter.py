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

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_count = len(initial_products)

        # Click on the "Tables" tab
        tables_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # Verify that at least one product appears after filtering
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        tables_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        tables_count = len(tables_products)
        self.assertGreater(tables_count, 0, "No products found after filtering by Tables")

        # Click on the "Chairs" tab
        chairs_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # Verify that product list is updated
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        chairs_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        chairs_count = len(chairs_products)
        self.assertGreater(chairs_count, 0, "No products found after filtering by Chairs")
        self.assertNotEqual(tables_count, chairs_count, "Product count did not change after filtering by Chairs")

        # Click "All" to remove the filter
        all_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # Confirm that the full list of products is shown
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
        )
        all_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        all_count = len(all_products)
        self.assertEqual(initial_count, all_count, "Product count is not equal to initial count after clicking All")


if __name__ == "__main__":
    unittest.main()