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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        try:
            # Accept cookies if the banner is present
            try:
                cookie_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
                )
                cookie_button.click()
            except:
                pass

            # Get initial product count
            product_wraps = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            initial_product_count = len(product_wraps)

            # Find and click the "Tables" filter tab
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()

            # Wait for the products to load after filtering
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
            )

            # Get the product count after filtering
            product_wraps_filtered = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            filtered_product_count = len(product_wraps_filtered)

            # Assert that at least one product is displayed after filtering
            self.assertGreater(filtered_product_count, 0, "No products displayed after filtering.")

            # Assert that the product count has changed after filtering
            self.assertNotEqual(initial_product_count, filtered_product_count,
                                "Product count did not change after filtering.")

        except Exception as e:
            self.fail(f"Test failed: {e}")


if __name__ == "__main__":
    unittest.main()