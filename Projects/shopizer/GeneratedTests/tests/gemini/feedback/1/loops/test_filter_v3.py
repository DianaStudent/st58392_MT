import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page.
        # Already done in setUp

        # Define a function to click tabs and count products
        def click_tab_and_count_products(tab_text):
            tab_locator = (By.XPATH, f"//a[text()='{tab_text}']")
            try:
                tab = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(tab_locator)
                )
                tab.click()
            except:
                self.fail(f"{tab_text} tab not found")

            product_locator = (By.XPATH, "//div[@class='product-wrap-2 mb-25']")
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(product_locator)
                )
            except:
                self.fail(f"Product grid did not update after applying '{tab_text}' filter")

            products = self.driver.find_elements(*product_locator)
            product_count = len(products)
            self.assertTrue(product_count > 0, f"No products displayed after applying '{tab_text}' filter")
            return product_count

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_product_count = click_tab_and_count_products("Tables")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        chairs_product_count = click_tab_and_count_products("Chairs")

        # 6. Verify that the list of products is updated and different from the previous.
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter")

        # 7. Then click the "All" filter to reset.
        all_product_count = click_tab_and_count_products("All")

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertTrue(all_product_count > tables_product_count, "Product count after 'All' filter is not greater than 'Tables' filter")
        self.assertTrue(all_product_count > chairs_product_count, "Product count after 'All' filter is not greater than 'Chairs' filter")

if __name__ == "__main__":
    unittest.main()