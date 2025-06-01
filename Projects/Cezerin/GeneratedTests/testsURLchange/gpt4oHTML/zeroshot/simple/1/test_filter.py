import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_filter_products(self):
        driver = self.driver
        
        # Locate and click "Brand A" checkbox
        try:
            brand_a_checkbox = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute']//label[input[@type='checkbox'] and contains(., 'Brand A')]//input"))
            )
        except Exception:
            self.fail("Brand A checkbox is not present")

        brand_a_checkbox.click()
        time.sleep(2)  # Wait for filter to apply
        
        # Check number of products displayed
        products_after_brand_a = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']//div[contains(@class, 'available')]"))
        )
        num_products_after_brand_a = len(products_after_brand_a)
        
        # Verify that the number of visible products changes
        self.assertNotEqual(num_products_after_brand_a, 2, "Number of products should change after filter is applied")

        # Uncheck "Brand A" checkbox
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for filter to revert
        
        # Check number of products displayed again
        products_after_unchecking = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']//div[contains(@class, 'available')]"))
        )
        num_products_after_unchecking = len(products_after_unchecking)

        # Assert to validate the number of products is back to original
        self.assertEqual(num_products_after_unchecking, 2, "Number of products should revert after filter is removed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()