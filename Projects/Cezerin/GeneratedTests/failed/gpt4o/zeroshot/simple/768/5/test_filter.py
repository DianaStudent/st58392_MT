from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Wait for the Brand A checkbox and click it
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[label[text()='Brand A']]/label/input")))
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to find Brand A checkbox: {str(e)}")
        
        time.sleep(2) # Wait for the filter to apply
        
        # Get the number of product cards visible
        product_cards_after_brand_a = driver.find_elements(By.CSS_SELECTOR, ".products .column.is-fullhd.available")
        initial_count = len(product_cards_after_brand_a)
        
        # Verify the number of product cards has changed
        if initial_count != 1:
            self.fail("Number of products did not change after applying Brand A filter")
        
        # Uncheck the Brand A filter
        brand_a_checkbox.click()
        time.sleep(2) # Wait for the filter to apply
        
        # Get the number of product cards visible again
        product_cards_after_unchecking = driver.find_elements(By.CSS_SELECTOR, ".products .column.is-fullhd.available")
        final_count = len(product_cards_after_unchecking)
        
        # Verify the number of product cards has returned to original
        if final_count != 2:
            self.fail("Number of products did not reset after removing Brand A filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()