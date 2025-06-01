from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Close cookie consent if present
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            if cookie_button.is_displayed():
                cookie_button.click()
        except:
            pass  # Continue if cookie consent button is not found

        # Filter by Tables
        tables_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']/h4")))
        tables_tab.click()

        # Wait for product grid to update
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='product-wrap-2']")
        ))

        # Count visible products
        table_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2']")
        self.assertEqual(len(table_products), 1, "Table filter should show 1 product.")

        # Filter by Chairs
        chairs_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']/h4")))
        chairs_tab.click()

        # Wait for product grid to update
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='product-wrap-2']")
        ))

        # Count visible products
        chair_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2']")
        self.assertEqual(len(chair_products), 3, "Chairs filter should show 3 products.")
        self.assertNotEqual(table_products, chair_products, "Product lists should differ between filters.")

        # Reset filter by clicking "All"
        all_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']/h4")))
        all_tab.click()

        # Wait for product grid to update
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='product-wrap-2']")
        ))

        # Count visible products
        all_products = driver.find_elements(By.XPATH, "//div[@class='product-wrap-2']")
        self.assertEqual(len(all_products), 4, "All filter should show 4 products.")

        # Verify "All" filter resets to all products
        self.assertGreater(len(all_products), len(table_products), "All products should be more than filtered ones.")

if __name__ == "__main__":
    unittest.main()