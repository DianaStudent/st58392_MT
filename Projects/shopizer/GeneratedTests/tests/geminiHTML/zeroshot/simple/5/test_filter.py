import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the banner is present
        try:
            cookie_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_count = len(initial_products)

        # Find and click the "Tables" filter tab
        try:
            tables_tab = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find or click the 'Tables' filter tab.")

        # Wait for the products to be filtered
        try:
            wait.until(
                lambda driver: len(driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")) > 0
            )
        except:
            self.fail("Products did not load after filtering.")

        # Get the filtered product count
        filtered_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        filtered_count = len(filtered_products)

        # Assert that at least one product is displayed after filtering
        self.assertGreater(filtered_count, 0, "No products displayed after filtering.")

        # Assert that the product count changed after filtering
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering.")


if __name__ == "__main__":
    unittest.main()