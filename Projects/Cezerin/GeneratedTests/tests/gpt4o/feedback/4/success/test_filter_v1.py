import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Verify the product cards are loaded
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        if not product_cards or len(product_cards) == 0:
            self.fail("Initial product cards are missing or not visible")

        initial_product_count = len(product_cards)

        # Apply "Brand A" filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input")))
        ActionChains(driver).move_to_element(brand_a_checkbox).click().perform()
        time.sleep(2)

        # Verify the product count changes
        filtered_product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        filtered_product_count = len(filtered_product_cards)

        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying Brand A filter")

        # Uncheck "Brand A" filter
        ActionChains(driver).move_to_element(brand_a_checkbox).click().perform()
        time.sleep(2)

        # Verify the original product count is restored
        restored_product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        restored_product_count = len(restored_product_cards)

        self.assertEqual(initial_product_count, restored_product_count, "Product count did not restore after unchecking Brand A filter")

        # Locate price slider and apply price range filter
        price_slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price-filter")))
        if not price_slider:
            self.fail("Price slider component is missing")

        # Assuming we have a mechanism to move the slider
        slider_handle = price_slider.find_element(By.XPATH, ".//div[contains(@class, 'handle')]")
        ActionChains(driver).drag_and_drop_by_offset(slider_handle, 10, 0).perform()
        time.sleep(2)

        # Verify the product count changes after applying price filter
        price_filtered_product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        price_filtered_product_count = len(price_filtered_product_cards)
        self.assertNotEqual(restored_product_count, price_filtered_product_count, "Product count did not change after applying price range filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()