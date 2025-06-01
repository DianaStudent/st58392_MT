import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_apply_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Locate and apply the "Brand A" checkbox filter
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input[@type='checkbox']")))
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate/operate Brand A checkbox: {str(e)}")

        # Wait to allow UI to update
        time.sleep(2)

        # Verify that the number of displayed product cards changes
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not product_cards:
            self.fail("No products found after applying Brand A filter.")
        original_count = len(product_cards)
        self.assertNotEqual(original_count, 2, "Expected product count to change after applying Brand A filter.")

        # Uncheck the "Brand A" filter
        try:
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate/operate Brand A checkbox: {str(e)}")

        # Wait to allow UI to update
        time.sleep(2)

        # Verify that the original number of product cards is restored
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not product_cards:
            self.fail("No products found after unchecking Brand A filter.")
        restored_count = len(product_cards)
        self.assertEqual(restored_count, 2, "Expected 2 product cards after unchecking Brand A filter.")

        # Locate the price element (slider).
        try:
            price_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".columns.is-mobile.is-gapless.price-filter-values .column")))
            self.assertTrue(price_slider, "Price slider not found.")
        except Exception as e:
            self.fail(f"Failed to locate price slider: {str(e)}")

        # Move the price slider to filter by price
        action = ActionChains(driver)
        action.move_to_element(price_slider).click_and_hold().move_by_offset(-30, 0).release().perform()

        # Wait to allow UI to update
        time.sleep(2)

        # Verify that the product count changes again
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not product_cards:
            self.fail("No products found after applying price filter.")
        self.assertNotEqual(len(product_cards), restored_count, "Expected product count to change after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()