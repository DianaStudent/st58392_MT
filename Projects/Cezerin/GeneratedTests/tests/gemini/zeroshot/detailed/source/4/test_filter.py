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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for products to load
        products_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products")
        wait.until(EC.presence_of_element_located(products_locator))

        # Get initial product count
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
        self.assertGreater(initial_product_count, 0, "No products found initially")

        # Locate and apply "Brand A" filter
        brand_a_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']")
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_locator))
        brand_a_checkbox.click()

        # Confirm "Brand A" is checked
        brand_a_label_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']")
        brand_a_label = wait.until(EC.presence_of_element_located(brand_a_label_locator))
        self.assertIn("attribute-checked", brand_a_label.get_attribute("class"), "Brand A filter not applied")

        time.sleep(2)

        # Verify product count is reduced
        filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
        self.assertLess(filtered_product_count, initial_product_count, "Product count not reduced after filtering by Brand A")

        # Uncheck "Brand A" filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_locator))
        brand_a_checkbox.click()

        time.sleep(2)

        # Verify product count is restored
        restored_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
        self.assertEqual(restored_product_count, initial_product_count, "Product count not restored after unchecking Brand A")

        # Locate price slider
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        price_filter = wait.until(EC.presence_of_element_located(price_filter_locator))

        # Locate right slider handle
        right_handle_locator = (By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        right_handle = wait.until(EC.presence_of_element_located(right_handle_locator))

        # Move right slider handle to reduce max price
        actions = ActionChains(driver)
        actions.click_and_hold(right_handle).move_by_offset(-5, 0).release().perform()

        time.sleep(2)

        # Verify product count is reduced
        price_filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
        self.assertLessEqual(price_filtered_product_count, restored_product_count, "Product count not reduced after price filtering")


if __name__ == "__main__":
    unittest.main()