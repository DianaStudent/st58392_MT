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

    def test_apply_product_filters(self):
        driver = self.driver
        wait = self.wait

        def get_product_count():
            product_cards = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".products .column.available")))
            return len(product_cards)

        # Verify and store the initial number of product cards
        initial_count = get_product_count()
        self.assertGreater(initial_count, 0, "No initial product cards found")

        # Locate and click the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(.,'Brand A')]/input")))
        driver.execute_script("arguments[0].click();", brand_a_checkbox)

        # Wait for UI to update
        time.sleep(2)

        # Verify that the number of product cards changes
        filtered_count = get_product_count()
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering")

        # Uncheck the "Brand A" filter
        driver.execute_script("arguments[0].click();", brand_a_checkbox)

        # Wait for UI to update
        time.sleep(2)

        # Verify that the number of product cards is restored
        restored_count = get_product_count()
        self.assertEqual(restored_count, initial_count, "Product count did not restore after unchecking filter")

        # Locate and move the price slider
        price_slider_left = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".price-filter-values .column.has-text-left")))
        action = ActionChains(driver)
        action.click_and_hold(price_slider_left).move_by_offset(20, 0).release().perform()

        # Wait for UI to update
        time.sleep(2)

        # Verify that the product count changes again
        final_count = get_product_count()
        self.assertNotEqual(final_count, restored_count, "Product count did not change after price adjustment")


if __name__ == "__main__":
    unittest.main()