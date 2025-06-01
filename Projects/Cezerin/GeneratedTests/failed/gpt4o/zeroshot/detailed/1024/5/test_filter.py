from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_apply_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Ensure products are loaded
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")))

        # Check initial product count
        initial_product_count = len(products)
        if initial_product_count == 0:
            self.fail("No products found in initial load.")

        # Step 2: Apply "Brand A" filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[.//input[@type='checkbox' and following-sibling::text()='Brand A']]")))
        brand_a_checkbox.click()

        # Verify it is checked
        self.assertTrue(brand_a_checkbox.find_element(By.CSS_SELECTOR, "input").is_selected())

        # Wait and verify number of products is reduced
        WebDriverWait(driver, 2)
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        filtered_product_count = len(filtered_products)
        self.assertLess(filtered_product_count, initial_product_count, "Product count did not reduce after applying Brand A filter.")

        # Uncheck the filter
        brand_a_checkbox.click()

        # Verify product count is restored
        WebDriverWait(driver, 2)
        products_restored = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        restored_product_count = len(products_restored)
        self.assertEqual(restored_product_count, initial_product_count, "Product count not restored after unchecking Brand A filter.")
        
        # Step 3: Adjust price slider
        slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-filter-values")))
        action = ActionChains(driver)

        # Locate the right slider handle and move it
        slider_handle = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='slider-handle'])[last()]")))
        action.click_and_hold(slider_handle).move_by_offset(-40, 0).release().perform()

        # Verify number of products is reduced after changing price range
        WebDriverWait(driver, 2)
        priced_filtered_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available")
        priced_filtered_count = len(priced_filtered_products)
        self.assertLess(priced_filtered_count, initial_product_count, "Product count did not reduce after adjusting price filter.")

if __name__ == "__main__":
    unittest.main()