import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # Find the Brand A checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
        except:
            self.fail("Brand A checkbox not found")

        # Get initial product count
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'column') and contains(@class, 'is-3-desktop') and contains(@class, 'available')]")
        initial_product_count = len(products)

        # Click the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after Brand A filter
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'column') and contains(@class, 'is-3-desktop') and contains(@class, 'available')]")
        filtered_product_count = len(products)

        # Uncheck the Brand A checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
        except:
            self.fail("Brand A checkbox not found")
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after unchecking Brand A filter
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'column') and contains(@class, 'is-3-desktop') and contains(@class, 'available')]")
        unfiltered_product_count = len(products)

        # Assert that the product count changed after filtering and unfiltering
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count is not equal to initial count after removing the filter")

        # Price Filter
        # Drag the price slider to change the price range.
        # Since there is no slider element, we cannot interact with it.
        # This part is skipped.

if __name__ == "__main__":
    unittest.main()