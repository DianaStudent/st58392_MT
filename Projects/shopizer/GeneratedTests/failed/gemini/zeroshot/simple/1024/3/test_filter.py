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

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the "Tables" filter tab and click it
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Could not find or click the 'Tables' filter tab.")

        # Get the initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
        initial_product_count = len(initial_products)

        # Find the "Chairs" filter tab and click it
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Could not find or click the 'Chairs' filter tab.")

        # Get the final product count
        final_products = driver.find_elements(By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6']")
        final_product_count = len(final_products)

        # Assert that at least one product is displayed
        self.assertGreater(final_product_count, 0, "No products displayed after filtering.")

        # Assert that the product count changes after applying filters
        self.assertNotEqual(initial_product_count, final_product_count, "Product count did not change after filtering.")


if __name__ == "__main__":
    unittest.main()