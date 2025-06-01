import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)  # Implicit wait to handle dynamic content
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies if button is present
        try:
            accept_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass
        
        # Locate and click on the "Tables" filter tab
        tables_tab = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]')
        ))
        tables_tab.click()

        # Wait for product grid to update
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.tab-content .tab-pane.active.show .product-wrap-2')
        ))

        # Store number of visible products for "Tables" filter
        table_products = driver.find_elements(By.CSS_SELECTOR, 
            '.tab-content .tab-pane.active.show .product-wrap-2'
        )
        table_product_count = len(table_products)
        self.assertEqual(table_product_count, 1, f"Expected 1 product, but got {table_product_count}")

        # Locate and click on the "Chairs" filter tab
        chairs_tab = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[data-rb-event-key="chairs"]')
        ))
        chairs_tab.click()

        # Wait for product grid to refresh
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.tab-content .tab-pane.active.show .product-wrap-2')
        ))

        # Store number of visible products for "Chairs" filter
        chair_products = driver.find_elements(By.CSS_SELECTOR, 
            '.tab-content .tab-pane.active.show .product-wrap-2'
        )
        chair_product_count = len(chair_products)
        self.assertEqual(chair_product_count, 3, f"Expected 3 products, but got {chair_product_count}")

        # Ensure the product list is different from "Tables" filter
        self.assertNotEqual(
            table_product_count, chair_product_count,
            "Product list for 'Tables' should not be the same as 'Chairs'"
        )

        # Locate and click on the "All" filter tab
        all_tab = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[data-rb-event-key="all"]')
        ))
        all_tab.click()

        # Wait for product grid to refresh
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.tab-content .tab-pane.active.show .product-wrap-2')
        ))

        # Store number of visible products for "All" filter
        all_products = driver.find_elements(By.CSS_SELECTOR, 
            '.tab-content .tab-pane.active.show .product-wrap-2'
        )
        all_product_count = len(all_products)
        self.assertEqual(all_product_count, 4, f"Expected 4 products, but got {all_product_count}")

        # Confirm that product list contains more items than after previous filters
        self.assertGreater(all_product_count, chair_product_count,
            "The 'All' filter product count should be greater than 'Chairs' filter"
        )

if __name__ == "__main__":
    unittest.main()