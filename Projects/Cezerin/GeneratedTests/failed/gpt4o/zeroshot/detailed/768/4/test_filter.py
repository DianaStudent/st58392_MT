from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products(self):
        driver = self.driver
        wait = self.wait

        # Wait for products and filters to be fully loaded
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products")))
        brand_filter_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox'] and contains(., 'Brand A')]/input")))

        # Apply the "Brand A" filter
        brand_filter_input.click()
        self.assertTrue(brand_filter_input.is_selected())
        self.driver.implicitly_wait(2)

        # Verify that the number of product cards is reduced
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 when Brand A filter is applied.")

        # Uncheck the "Brand A" filter
        brand_filter_input.click()
        self.assertFalse(brand_filter_input.is_selected())
        self.driver.implicitly_wait(2)

        # Verify product count is restored
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 2, "Product count should be restored to 2 when Brand A filter is removed.")

        # Locate the price slider and move the right slider handle
        price_slider = driver.find_element(By.CSS_SELECTOR, ".price-filter .columns.is-gapless")
        right_handle = driver.find_element(By.CSS_SELECTOR, ".noUi-handle.noUi-handle-upper")

        # Move the right slider handle
        ActionChains(driver).click_and_hold(right_handle).move_by_offset(-20, 0).release().perform()
        
        # Wait briefly to allow products to update
        self.driver.implicitly_wait(2)

        # Verify that the number of product cards is reduced to 1
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 when price slider is applied.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()