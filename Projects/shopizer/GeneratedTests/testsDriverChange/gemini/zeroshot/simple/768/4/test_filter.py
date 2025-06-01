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

        # Accept cookies if the consent banner is present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
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
        except Exception as e:
            self.fail(f"Could not click 'Tables' tab: {e}")

        # Get the number of products displayed before filtering
        products_before_filter = len(driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']"))

        # Find the 'Chairs' filter tab and click it
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Chairs' tab: {e}")

        # Get the number of products displayed after filtering
        products_after_filter = len(driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']"))

        # Assert that at least one product is displayed after filtering
        self.assertGreater(products_after_filter, 0, "No products are displayed after filtering.")

        # Assert that the product count changes after applying filters
        self.assertNotEqual(products_before_filter, products_after_filter, "Product count did not change after filtering.")


if __name__ == "__main__":
    unittest.main()