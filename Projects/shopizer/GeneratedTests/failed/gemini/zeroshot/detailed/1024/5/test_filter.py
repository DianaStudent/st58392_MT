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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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

        # 2. Apply the "Tables" filter
        tables_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Wait for product grid to update and check at least one product is displayed
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
        )
        tables_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")
        tables_product_count = len(tables_products)

        if tables_product_count == 0:
            self.fail("No products displayed after applying 'Tables' filter.")

        # 5. Switch to the "Chairs" filter
        chairs_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # Wait for product grid to update and check at least one product is displayed
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
        )
        chairs_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")
        chairs_product_count = len(chairs_products)

        if chairs_product_count == 0:
            self.fail("No products displayed after applying 'Chairs' filter.")

        # 6. Verify that the list of products is updated and different from the previous.
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset
        all_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # Wait for product grid to update and check at least one product is displayed
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]"))
        )

        all_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//a[contains(@href, '/product/')]")
        all_product_count = len(all_products)

        if all_product_count == 0:
            self.fail("No products displayed after applying 'All' filter.")

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertGreater(all_product_count, tables_product_count, "Product count after 'All' filter is not greater than after 'Tables' filter.")
        self.assertGreater(all_product_count, chairs_product_count, "Product count after 'All' filter is not greater than after 'Chairs' filter.")

if __name__ == "__main__":
    unittest.main()