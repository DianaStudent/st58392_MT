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

        # Accept cookies if the banner is present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the 'All' tab and get the initial product count
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
            initial_products = driver.find_elements(By.CLASS_NAME, "product-wrap-2")
            initial_product_count = len(initial_products)
        except:
            self.fail("Could not find 'All' tab or get initial product count")
            return

        # Find the 'Tables' tab and click it
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find 'Tables' tab")
            return

        # Wait for the products to load and get the new product count
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
            )
            filtered_products = driver.find_elements(By.CLASS_NAME, "product-wrap-2")
            filtered_product_count = len(filtered_products)
        except:
            self.fail("Products did not load after filtering")
            return

        # Assert that at least one product is displayed after filtering
        self.assertGreater(filtered_product_count, 0, "No products displayed after filtering")

        # Assert that the product count changed after filtering
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering")


if __name__ == "__main__":
    unittest.main()