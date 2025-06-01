import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filtering(self):
        driver = self.driver

        # Locate the Brand A checkbox filter
        try:
            brand_a_checkbox = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Brand A')]/input[@type='checkbox']"))
            )
        except:
            self.fail("Brand A checkbox is missing.")
        
        # Count product cards before applying Brand A filter
        product_cards_before = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
        initial_product_count = len(product_cards_before)
        if initial_product_count == 0:
            self.fail("Product cards are missing before applying filters.")

        # Apply the Brand A filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify number of product cards after filter
        product_cards_after_brand_filter = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
        filtered_product_count = len(product_cards_after_brand_filter)
        self.assertNotEqual(filtered_product_count, initial_product_count, "Product count did not change after applying Brand A filter.")
        
        # Uncheck Brand A filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify original number of product cards is restored
        product_cards_after_unchecking = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
        restored_product_count = len(product_cards_after_unchecking)
        self.assertEqual(restored_product_count, initial_product_count, "Product count did not restore after removing Brand A filter.")

        # Locate the price slider component
        try:
            price_slider = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-filter-values"))
            )
        except:
            self.fail("Price slider component is missing.")
 
        # Move a slider handle to apply a price range filter
        try:
            # Assuming there are slider handles to interact with
            slider_handles = driver.find_elements(By.CSS_SELECTOR, ".rc-slider-handle")
            # Verify slider handle presence
            if not slider_handles:
                self.fail("Slider handles are missing.")
            action = ActionChains(driver)
            action.click_and_hold(slider_handles[0]).move_by_offset(-30, 0).release().perform()
            time.sleep(2)
        except:
            self.fail("Slider handle is missing or not interactive.")

        # Verify product count changes after price filter
        product_cards_after_price_filter = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
        price_filtered_product_count = len(product_cards_after_price_filter)
        self.assertNotEqual(price_filtered_product_count, restored_product_count, "Product count did not change after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()