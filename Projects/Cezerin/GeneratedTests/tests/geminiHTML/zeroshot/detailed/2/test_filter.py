import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # Wait for products to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "products"))
        )

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]")
        initial_product_count = len(initial_products)
        self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")

        # Locate and apply "Brand A" filter
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # Confirm "Brand A" is checked by checking the class of the label changes
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[contains(@class, 'attribute-checked')]"))
        )

        time.sleep(2)

        # Verify product count is reduced
        filtered_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]")
        filtered_product_count = len(filtered_products)
        self.assertTrue(filtered_product_count >= 0, "Filtered product count should be greater than or equal to 0")
        self.assertLess(filtered_product_count, initial_product_count, "Product count should be reduced after filtering")

        # Uncheck "Brand A" filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # Confirm "Brand A" is unchecked by checking the class of the label changes
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[not(contains(@class, 'attribute-checked'))]"))
        )

        # Verify product count is restored
        restored_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]")
        restored_product_count = len(restored_products)
        self.assertEqual(restored_product_count, initial_product_count, "Product count should be restored after unchecking filter")

        # Locate price slider and move handle
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        price_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )

        # Locate the right slider handle
        right_handle_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        right_handle = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(right_handle_locator)
        )

        # Get the current max price
        max_price = right_handle.text.replace('$', '').replace(',', '')
        max_price = float(max_price)

        # Calculate the offset to move the slider to the desired price
        desired_price = 1159.00
        if desired_price >= max_price:
            print("Desired price is greater than or equal to the maximum price. Skipping slider movement.")
            return

        # Move the slider
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(right_handle, -20, 0).perform()

        time.sleep(2)

        # Verify product count is reduced
        price_filtered_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]")
        price_filtered_product_count = len(price_filtered_products)
        self.assertTrue(price_filtered_product_count >= 0, "Price Filtered product count should be greater than or equal to 0")
        self.assertLessEqual(price_filtered_product_count, restored_product_count, "Product count should be reduced after price filtering")

if __name__ == "__main__":
    unittest.main()