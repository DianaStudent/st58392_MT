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
            cookie_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the 'All' products tab and count the products
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
            all_products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']"))
            )
            initial_product_count = len(all_products)
        except:
            self.fail("Could not find 'All' tab or products")

        # Find the 'Tables' filter tab and click it
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find 'Tables' tab")

        # Wait for the products to load after filtering
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']"))
            )
        except:
            self.fail("Products did not load after filtering")

        # Count the products after filtering
        try:
            filtered_products = driver.find_elements(By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
            filtered_product_count = len(filtered_products)
        except:
            self.fail("Could not count products after filtering")

        # Assert that at least one product is displayed after filtering
        self.assertGreater(filtered_product_count, 0, "No products displayed after filtering")

        # Assert that the product count has changed after applying the filter
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering")


if __name__ == "__main__":
    unittest.main()