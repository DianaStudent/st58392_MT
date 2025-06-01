import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # Get initial number of products
        products = WebDriverWait(driver, 20).until(
            EC.presence_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        initial_product_count = len(products)
        print(f"Initial product count: {initial_product_count}")

        # Find the Brand A checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )

        # Click the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Get the number of products after filtering
        products_after_filter = WebDriverWait(driver, 20).until(
            EC.presence_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        product_count_after_filter = len(products_after_filter)
        print(f"Product count after filter: {product_count_after_filter}")

        # Verify that the number of products has changed
        self.assertNotEqual(initial_product_count, product_count_after_filter, "Product count did not change after applying filter.")

        # Uncheck the Brand A checkbox
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Get the number of products after removing the filter
        products_after_uncheck = WebDriverWait(driver, 20).until(
            EC.presence_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        product_count_after_uncheck = len(products_after_uncheck)
        print(f"Product count after uncheck: {product_count_after_uncheck}")

        # Verify that the number of products has changed back to the initial count
        self.assertEqual(initial_product_count, product_count_after_uncheck, "Product count did not change back after removing filter.")

if __name__ == "__main__":
    unittest.main()