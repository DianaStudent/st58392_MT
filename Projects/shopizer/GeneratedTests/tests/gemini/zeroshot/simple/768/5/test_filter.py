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

        # Find the 'Tables' filter tab and click it
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find or click 'Tables' filter tab.")

        # Get the initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        initial_product_count = len(initial_products)

        # Check that at least one product is displayed after filter applied
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
            )
        except:
            self.fail("No products displayed after applying 'Tables' filter.")

        # Get the product count after filter applied
        filtered_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        filtered_product_count = len(filtered_products)

        # Assert that product count changed after applying filter
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filter applied.")

if __name__ == "__main__":
    unittest.main()