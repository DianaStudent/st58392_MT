import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Accept cookies if the consent banner is present
        try:
            cookie_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_count = len(initial_products)

        # Find the "Tables" filter tab and click it
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find or click the 'Tables' filter tab.")

        # Wait for the products to load after applying the filter
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
            )
        except:
            self.fail("Products did not load after applying the 'Tables' filter.")

        # Get the product count after applying the filter
        filtered_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        filtered_count = len(filtered_products)

        # Verify that at least one product is displayed after filtering
        self.assertGreater(filtered_count, 0, "No products are displayed after applying the 'Tables' filter.")

        # Assert that the product count has changed after applying the filter
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after applying the filter.")


if __name__ == "__main__":
    unittest.main()