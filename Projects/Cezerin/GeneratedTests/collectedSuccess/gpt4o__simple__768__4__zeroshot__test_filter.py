from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_apply_product_filter(self):
        driver = self.driver

        try:
            # Locate and click the "Brand A" checkbox
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Brand A')]//input"))
            )
            brand_a_checkbox.click()

            # Wait for the filter to apply and verify the number of visible product cards
            time.sleep(2)  # Adding a sleep to simulate some delay for the UI to update
            products_after_filter = driver.find_elements(By.CLASS_NAME, "available")
            self.assertEqual(len(products_after_filter), 1, "Filter did not apply correctly.")

            # Uncheck the "Brand A" checkbox
            brand_a_checkbox.click()

            # Wait for the filter to remove and verify the number of visible product cards
            time.sleep(2)  # Adding a sleep to simulate some delay for the UI to update
            products_after_unfilter = driver.find_elements(By.CLASS_NAME, "available")
            self.assertEqual(len(products_after_unfilter), 2, "Filter did not remove correctly.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()