import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_apply_brand_a_filter(self):
        driver = self.driver
        wait = self.wait

        # Verify the initial number of product cards
        product_cards = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".products .column.available")))
        initial_count = len(product_cards)
        self.assertTrue(initial_count > 0, "No initial product cards found")

        # Locate and click the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[input[@type='checkbox'] and text()[contains(., 'Brand A')]]/input")))
        driver.execute_script("arguments[0].click();", brand_a_checkbox)

        # Wait for UI to update
        time.sleep(2)

        # Verify that the number of product cards changes
        filtered_product_cards = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".products .column.available")))
        filtered_count = len(filtered_product_cards)
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering")
        self.assertTrue(filtered_count < initial_count, "Filtered count should be less than initial count")

        # Uncheck the "Brand A" filter
        driver.execute_script("arguments[0].click();", brand_a_checkbox)

        # Wait for UI to update
        time.sleep(2)

        # Verify that the number of product cards is restored
        restored_product_cards = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".products .column.available")))
        restored_count = len(restored_product_cards)
        self.assertEqual(restored_count, initial_count, "Product count did not restore after unchecking filter")

        # Locate and adjust the price slider
        price_slider_left = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".price-filter .column.has-text-left")))
        action = ActionChains(driver)
        action.click_and_hold(price_slider_left).move_by_offset(10, 0).release().perform()

        # Wait for UI to update
        time.sleep(2)

        # Verify that the product count changes again
        final_product_cards = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".products .column.available")))
        final_count = len(final_product_cards)
        self.assertNotEqual(final_count, restored_count, "Product count did not change after price adjustment")

if __name__ == "__main__":
    unittest.main()