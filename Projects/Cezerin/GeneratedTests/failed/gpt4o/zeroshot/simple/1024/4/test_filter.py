from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')

    def test_filter_by_brand_and_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Locate Brand A checkbox
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Brand A')]/input")))
        self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox is missing")

        # Get initial number of products
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        initial_count = len(initial_products)

        # Click on Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Check the number of visible products after applying the Brand A filter
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        filtered_count = len(filtered_products)
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering by Brand A")

        # Uncheck the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Check the number of products back to original after removing the filter
        unfiltered_products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        unfiltered_count = len(unfiltered_products)
        self.assertEqual(initial_count, unfiltered_count, "Product count did not revert after unchecking Brand A filter")

        # Locate price slider and adjust it
        price_slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']")))
        self.assertIsNotNone(price_slider, "Price slider is missing")

        action = ActionChains(driver)
        slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='noUi-handle']")))
        action.click_and_hold(slider).move_by_offset(-30, 0).release().perform()
        time.sleep(2)

        # Verify the product count changes again
        price_filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        price_filtered_count = len(price_filtered_products)
        self.assertNotEqual(initial_count, price_filtered_count, "Product count did not change after adjusting the price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()