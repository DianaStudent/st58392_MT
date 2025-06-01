from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/category-a")

    def test_filter_by_brand(self):
        # Apply "Brand A" filter
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Brand A']"))).click()

        WebDriverWait(self.driver, 2) # wait for UI to update

        original_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']"))
        
        # Uncheck "Brand A" filter
        self.driver.find_element(By.XPATH, "//input[@value='Brand A']").click()

        WebDriverWait(self.driver, 2) # wait for UI to update

        current_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-card']"))
        
        if original_count != current_count:
            self.fail("Product count did not match expected value.")

    def test_filter_by_price(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-slider-handle")))

        # Move one of the slider handles to apply a price range filter
        self.driver.find_element(By.CSS_SELECTOR, ".price-slider-handle").click()

        # wait for UI to update
        WebDriverWait(self.driver, 2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()