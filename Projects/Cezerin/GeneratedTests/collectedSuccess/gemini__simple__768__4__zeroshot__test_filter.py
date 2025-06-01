import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Function to count product cards
        def count_product_cards():
            product_elements = driver.find_elements(By.CSS_SELECTOR, ".products .column[class*='is-']")
            return len(product_elements)

        # Initial product count
        initial_product_count = count_product_cards()
        print(f"Initial product count: {initial_product_count}")

        # Find and click the "Brand A" checkbox
        try:
            brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
            print("Clicked Brand A checkbox")
        except Exception as e:
            self.fail(f"Could not click Brand A checkbox: {e}")

        # Wait for 2 seconds
        time.sleep(2)

        # Product count after Brand A filter
        filtered_product_count = count_product_cards()
        print(f"Product count after Brand A filter: {filtered_product_count}")
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after applying Brand A filter")

        # Uncheck "Brand A"
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
            print("Unclicked Brand A checkbox")
        except Exception as e:
            self.fail(f"Could not uncheck Brand A checkbox: {e}")

        # Wait for 2 seconds
        time.sleep(2)

        # Product count after unchecking Brand A filter
        unfiltered_product_count = count_product_cards()
        print(f"Product count after unchecking Brand A filter: {unfiltered_product_count}")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count should revert to initial count after unchecking Brand A filter")

        # Price filter
        try:
            price_filter_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
            price_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
            print(f"Price filter: {price_filter.text}")
        except Exception as e:
            self.fail(f"Could not find Price filter: {e}")

if __name__ == "__main__":
    unittest.main()