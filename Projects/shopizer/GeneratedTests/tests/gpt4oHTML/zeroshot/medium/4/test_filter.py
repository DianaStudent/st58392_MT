import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Assuming the base URL for your test

    def test_product_filters(self):
        driver = self.driver

        # Accept Cookies if the button exists
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            ).click()
        except Exception as e:
            self.fail("Accept cookies button not found or could not be clicked.")

        # Helper functions to count items in the current selection
        def get_product_count():
            try:
                products = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, ".product-wrap-2")
                    )
                )
                return len(products)
            except:
                return 0

        # Step 2: Click on the "Tables" tab to filter products
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
            )
            tables_tab.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".product-tab-list .nav-link.active")
                )
            )
        except Exception as e:
            self.fail("Tables filter tab not found or could not be clicked.")

        # Step 3: Verify at least one product appears for Tables
        tables_product_count = get_product_count()
        self.assertGreater(tables_product_count, 0, "No products displayed for Tables.")

        # Step 4: Click on the "Chairs" tab to change filter
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Chairs"))
            )
            chairs_tab.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".product-tab-list .nav-link.active")
                )
            )
        except Exception as e:
            self.fail("Chairs filter tab not found or could not be clicked.")

        # Step 5: Verify product list is updated for Chairs
        chairs_product_count = get_product_count()
        self.assertNotEqual(tables_product_count, chairs_product_count,
                               "Product count did not update after selecting Chairs.")

        # Step 6: Click "All" to remove filter
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "All"))
            )
            all_tab.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".product-tab-list .nav-link.active")
                )
            )
        except Exception as e:
            self.fail("All filter tab not found or could not be clicked.")

        # Step 7: Confirm the full list of products is shown
        all_product_count = get_product_count()
        self.assertGreater(all_product_count, max(tables_product_count, chairs_product_count),
                            "Product list not fully restored after removing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()