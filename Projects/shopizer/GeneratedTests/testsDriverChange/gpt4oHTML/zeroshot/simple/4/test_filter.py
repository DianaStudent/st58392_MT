import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")  # Replace with the correct URL

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_filter_products(self):
        driver = self.driver
        
        # Accept cookies if the button is present
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found: {str(e)}")

        # Get the original product count
        original_product_count = self.get_product_count()

        # Click on the 'Tables' filter tab
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Tables filter tab not found: {str(e)}")

        # Wait for the filter to be applied and check product count
        try:
            WebDriverWait(driver, 20).until(
                lambda d: self.get_product_count() != original_product_count
            )
            filter_applied_product_count = self.get_product_count()
            self.assertGreater(filter_applied_product_count, 0, "No products displayed after filter applied.")
        except Exception as e:
            self.fail(f"Failed to apply filter or no products found: {str(e)}")

    def get_product_count(self):
        driver = self.driver
        try:
            products = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            return len(products)
        except Exception:
            return 0

if __name__ == "__main__":
    unittest.main()