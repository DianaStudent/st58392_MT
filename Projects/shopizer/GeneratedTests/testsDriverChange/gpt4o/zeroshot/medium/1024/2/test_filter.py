import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        # Accept cookies if the consent banner exists
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#rcc-confirm-button")
                )
            )
            accept_cookies_button.click()
        except Exception:
            pass

    def test_product_filter(self):
        driver = self.driver

        # Click on the "Tables" tab
        tables_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-rb-event-key='tables']")
            )
        )
        tables_tab.click()

        # Verify that at least one product appears
        table_products = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
            )
        )
        self.assertGreater(len(table_products), 0, "No products found for 'Tables'")

        # Click on the "Chairs" tab
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-rb-event-key='chairs']")
            )
        )
        chairs_tab.click()

        # Verify that product list is updated
        chair_products = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
            )
        )
        self.assertGreater(len(chair_products), 0, "No products found for 'Chairs'")
        self.assertNotEqual(len(table_products), len(chair_products), "Product count did not change when filtering 'Chairs'")

        # Click "All" to remove the filter
        all_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-rb-event-key='all']")
            )
        )
        all_tab.click()

        # Confirm that the full list of products is shown
        all_products = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@role='tabpanel' and contains(@class, 'active')]//div[contains(@class, 'product-wrap-2')]")
            )
        )
        self.assertGreater(len(all_products), len(table_products), "Full product list is not displayed after removing filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()