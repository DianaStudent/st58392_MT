from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_and_verify_filters(self):
        driver = self.driver
        wait = self.wait

        # Wait for the products and filters to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products")))
        
        # Locate the "Brand A" checkbox and apply
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Brand A')]/input")))
        brand_a_checkbox.click()
        
        # Wait for filter application and confirm it's checked
        time.sleep(2)
        assert brand_a_checkbox.is_selected(), "Brand A checkbox should be selected"
        
        # Verify product count reduction
        products = driver.find_elements(By.CLASS_NAME, "product-name")
        self.assertEqual(len(products), 1, "There should be 1 product displayed after applying 'Brand A' filter")

        # Uncheck the filter
        brand_a_checkbox.click()
        time.sleep(2)
        
        # Verify product count restored
        products = driver.find_elements(By.CLASS_NAME, "product-name")
        self.assertEqual(len(products), 2, "There should be 2 products displayed after removing 'Brand A' filter")

        # Locate the price slider component and move right slider to new value
        price_slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price-filter")))
        slider_handle = price_slider.find_element(By.XPATH, ".//*[contains(@class, 'slider-handle-max')]")
        webdriver.ActionChains(driver).click_and_hold(slider_handle).move_by_offset(-10, 0).release().perform()
        
        # Wait for slider adjustment
        time.sleep(2)
        
        # Verify product count reduction again
        products = driver.find_elements(By.CLASS_NAME, "product-name")
        self.assertEqual(len(products), 1, "There should be 1 product displayed after adjusting price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()