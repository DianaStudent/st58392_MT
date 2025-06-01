from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a")

    def test_filter_brand_and_price(self):
        driver = self.driver

        # Wait for products and filters to load
        products_locator = (By.CLASS_NAME, "product-caption")
        filters_locator = (By.CLASS_NAME, "attribute-filter")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(products_locator))
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(filters_locator))

        # Check the number of products before filtering
        initial_product_count = len(driver.find_elements(By.CLASS_NAME, "product-caption"))
        self.assertTrue(initial_product_count > 0, "Initial products are not loaded")

        # Apply the "Brand A" filter
        brand_a_checkbox = driver.find_element(By.XPATH, "//label[contains(text(), 'Brand A')]//input")
        ActionChains(driver).move_to_element(brand_a_checkbox).click().perform()

        # Confirm Brand A checkbox is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not selected")

        # Wait 2 seconds and verify the number of product cards is reduced
        sleep(2)
        filtered_product_count = len(driver.find_elements(By.CLASS_NAME, "product-caption"))
        self.assertTrue(filtered_product_count < initial_product_count, "Products were not filtered by Brand A")

        # Uncheck the filter
        ActionChains(driver).move_to_element(brand_a_checkbox).click().perform()
        self.assertFalse(brand_a_checkbox.is_selected(), "Brand A checkbox is not deselected")

        # Wait 2 seconds and verify product count is restored
        sleep(2)
        restored_product_count = len(driver.find_elements(By.CLASS_NAME, "product-caption"))
        self.assertEqual(restored_product_count, initial_product_count, "Products were not restored after unchecking Brand A")

        # Locate the price slider and modify max price
        price_slider_max = driver.find_element(By.XPATH, "//input[@aria-valuemax='1250.00']")
        price_slider_min = driver.find_element(By.XPATH, "//input[@aria-valuemin='950.00']")
        
        # Verify price sliders exist
        self.assertIsNotNone(price_slider_max, "Max price slider is not present")
        self.assertIsNotNone(price_slider_min, "Min price slider is not present")

        # Move the right slider handle to change max price
        ActionChains(driver).click_and_hold(price_slider_max).move_by_offset(-50, 0).release().perform()

        # Wait 2 seconds and verify the number of product cards is reduced
        sleep(2)
        filtered_price_product_count = len(driver.find_elements(By.CLASS_NAME, "product-caption"))
        self.assertTrue(filtered_price_product_count < restored_product_count, "Products were not filtered by adjusted price")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()