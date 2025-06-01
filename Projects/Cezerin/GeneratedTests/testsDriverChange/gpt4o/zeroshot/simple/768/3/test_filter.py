import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_and_remove_brand_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Wait for and select "Brand A" filter checkbox
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title' and text()='Brand']/following-sibling::label[contains(.,'Brand A')]/input")))
            brand_a_checkbox.click()
            sleep(2)

            # Assert the number of visible products should be 1
            products_after_brand_filter = driver.find_elements(By.CSS_SELECTOR, ".columns.products .available")
            self.assertEqual(len(products_after_brand_filter), 1)

            # Uncheck "Brand A"
            brand_a_checkbox.click()
            sleep(2)

            # Assert the number of visible products should be back to 2
            products_after_unchecking = driver.find_elements(By.CSS_SELECTOR, ".columns.products .available")
            self.assertEqual(len(products_after_unchecking), 2)
            
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def test_price_slider(self):
        driver = self.driver
        wait = self.wait

        # Wait for and adjust price slider
        try:
            price_slider = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']//div[@class='price-filter-values']//div[1]")))
            # Perform slider adjustment e.g., using Actions class for drag_and_drop_by_offset (pseudo-code)
            # This requires an appropriate method from Selenium which handles slider interactions

            # Assert the number of visible products should change
            products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, ".columns.products .available")
            # Example validation (It depends on the slider action performed)
            self.assertEqual(len(products_after_price_filter), 1)

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()