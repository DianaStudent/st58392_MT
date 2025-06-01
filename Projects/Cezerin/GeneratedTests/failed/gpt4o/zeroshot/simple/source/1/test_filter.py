from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_apply_filter(self):
        driver = self.driver
        driver.get("http://localhost:3000/category-a")
        
        try:
            # Wait for and select Brand A filter
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Brand A')]/input"))
            )
            brand_a_checkbox.click()

            # Wait for the page to reflect the filter change
            time.sleep(2)

            # Count the number of products displayed
            products_after_brand_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products_after_brand_filter), 1, "There should be 1 product after applying Brand A filter")

            # Uncheck Brand A filter
            brand_a_checkbox.click()

            # Wait for the page to reflect the filter change
            time.sleep(2)

            # Count the number of products displayed
            products_after_removing_brand_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products_after_removing_brand_filter), 2, "There should be 2 products after removing Brand A filter")

            # Interact with price slider - Simulate price filter change
            # Please replace slider selector with realistic selector based on html structure

            # Assuming slider can be interacted by clicking at certain points
            price_slider = driver.find_element(By.CSS_SELECTOR, ".price-filter .attribute-title + .columns")
            webdriver.ActionChains(driver).drag_and_drop_by_offset(price_slider, -50, 0).perform()
            
            # Wait for the page to reflect the filter change
            time.sleep(2)

            # Count the number of products displayed after price filter adjustment
            products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products_after_price_filter), 1, "There should be 1 product after price filter adjustment")
        
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()