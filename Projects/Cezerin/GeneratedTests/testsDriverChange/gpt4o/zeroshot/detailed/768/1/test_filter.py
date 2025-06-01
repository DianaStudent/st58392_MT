import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilters(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_apply_brand_a_filter_and_price_slider(self):
        driver = self.driver

        # Wait until products and filters are fully loaded
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".section-category")))

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[input[@type='checkbox' and following-sibling::text() = 'Brand A']]")))
        brand_a_checkbox.click()
        time.sleep(2)
        
        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.get_attribute('class').find('attribute-checked') != -1, 
                        "Brand A checkbox is not checked.")
        
        # Verify that the number of product cards is reduced
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        self.assertEqual(len(products), 1, 
                         "Product count not reduced after applying Brand A filter.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm product count is restored
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        self.assertEqual(len(products), 2, 
                         "Product count not restored after removing Brand A filter.")

        # Locate the price slider component
        price_slider_handle = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@aria-valuemax='1250']")))
        
        # Create an action chain to move the slider
        ActionChains(driver).drag_and_drop_by_offset(price_slider_handle, -50, 0).perform()
        time.sleep(2)

        # Verify that the number of product cards is reduced
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        self.assertEqual(len(products), 1, 
                         "Product count not reduced after applying price filter.")

if __name__ == "__main__":
    unittest.main()