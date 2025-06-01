from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_apply_remove_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify initial product existence
        initial_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.products .column.available'))
        )
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("Initial products are not displayed")

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'attribute-title') and text()='Brand']/following-sibling::label[1]/input"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count after filter
        filtered_products = driver.find_elements(By.CSS_SELECTOR, '.products .column.available')
        filtered_product_count = len(filtered_products)
        self.assertNotEqual(filtered_product_count, initial_product_count, "Product count did not change after applying Brand A filter")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count is restored
        restored_products = driver.find_elements(By.CSS_SELECTOR, '.products .column.available')
        restored_product_count = len(restored_products)
        self.assertEqual(restored_product_count, initial_product_count, "Product count did not restore after removing Brand A filter")

        # Locate the price slider component
        price_slider = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.price-filter .columns.is-mobile.is-gapless'))
        )
        slider_handle = price_slider.find_element(By.XPATH, ".//div[contains(@class, 'column')][1]")
        actions = ActionChains(driver)
        actions.click_and_hold(slider_handle).move_by_offset(20, 0).release().perform()
        time.sleep(2)

        # Verify product count changes after applying price range
        price_filtered_products = driver.find_elements(By.CSS_SELECTOR, '.products .column.available')
        price_filtered_count = len(price_filtered_products)
        self.assertNotEqual(price_filtered_count, restored_product_count, "Product count did not change after applying price range filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()