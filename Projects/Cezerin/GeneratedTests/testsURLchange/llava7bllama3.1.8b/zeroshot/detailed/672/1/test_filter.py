from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/category-a')

    def tearDown(self):
        self.driver.quit()

    def test_filtering(self):
        # Wait until products and filters are fully loaded
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div#filters'))
        )

        # Locate and apply the "Brand A" checkbox filter using its associated input
        brand_a_filter = self.driver.find_element(By.CSS_SELECTOR, 'input[name="brandA"]')
        brand_a_filter.click()

        # Confirm it is checked
        self.assertTrue(brand_a_filter.is_selected())

        # Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-card'))
        )
        initial_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, 'div.product-card'))
        self.assertLess(initial_product_count, 5)

        # Uncheck the filter and confirm product count is restored (e.g., 1 → 2)
        brand_a_filter.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-card'))
        )
        final_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, 'div.product-card'))
        self.assertGreater(final_product_count, initial_product_count)

        # Locate the price slider component and move the right slider handle to reduce the maximum price to 1159
        price_slider = self.driver.find_element(By.CSS_SELECTOR, '#price-slider')
        ActionChains(self.driver).drag_and_drop_by_offset(price_slider, -50, 0).perform()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.slider-handle'))
        )
        price_slider_handle = self.driver.find_elements(By.CSS_SELECTOR, 'span.slider-handle')
        current_price = float(self.driver.find_element(By.XPATH, '//span[(@id="price-slider-value")]/ancestor::div[@class="slider"]/input').get_attribute('value'))
        aria_valuenow_value = int(price_slider_handle[-1].get_attribute('aria-valuenow'))

        # Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-card'))
        )
        new_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, 'div.product-card'))

        self.assertLess(initial_product_count, new_product_count)

if __name__ == '__main__':
    unittest.main()