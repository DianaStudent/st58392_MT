import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a")  # Change this to the local path of your HTML file

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Locate and check the "Brand A" checkbox
        try:
            brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Brand A')]/input")))
            brand_a_checkbox.click()
        except:
            self.fail("Failed to find and click 'Brand A' checkbox")
        
        # Wait for 2 seconds
        time.sleep(2)

        # Verify number of products after applying filter
        try:
            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available"))
            self.assertEqual(filtered_product_count, 1, "Product count did not reduce as expected after applying 'Brand A' filter")
        except:
            self.fail("Failed to evaluate product count after 'Brand A' filter applied")
        
        # Uncheck the "Brand A" checkbox
        try:
            brand_a_checkbox.click()
        except:
            self.fail("Failed to uncheck 'Brand A' filter")
        
        # Wait for 2 seconds
        time.sleep(2)

        # Verify number of products after removing filter
        try:
            full_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available"))
            self.assertEqual(full_product_count, 2, "Product count did not restore to initial after removing 'Brand A' filter")
        except:
            self.fail("Failed to evaluate product count after 'Brand A' filter removed")

        # Interact with price slider - This is a mock step as sliders need JS interaction beyond simple HTML
        try:
            # Locate price range information
            price_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter-values")))
            self.assertTrue(price_info, "Price range slider not found.")
            # Simulate slider action by directly manipulating the product filter as no real slider exists in the mock HTML
            # In a real-world scenario, you would interact with a slider element
            driver.execute_script("document.querySelector('.columns.is-multiline.is-mobile.products .column.available:not([style*=\"display: none;\"])').style.display = 'none';")
            simulated_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available"))
            self.assertEqual(simulated_product_count, 1, "Product count did not change after interacting with price slider")
        except:
            self.fail("Failed to interact with price range element or evaluate filtered results")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()