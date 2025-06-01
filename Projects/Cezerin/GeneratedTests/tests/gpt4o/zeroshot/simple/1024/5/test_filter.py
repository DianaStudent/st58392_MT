import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")

    def test_apply_filter(self):
        driver = self.driver

        try:
            # Wait for the page to load and the Brand A checkbox to be available
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Brand']/following-sibling::label[input[@type='checkbox'] and contains(text(), 'Brand A')]"))
            )
            
            # Apply Brand A filter
            brand_a_checkbox.click()
            time.sleep(2)  # Wait to see the change

            # Count the number of products after applying Brand A filter
            products_after_brand_a = len(driver.find_elements(By.CSS_SELECTOR, ".products .available"))
            
            # Remove Brand A filter
            brand_a_checkbox.click()
            time.sleep(2)  # Wait to see the change

            # Count the number of products after removing Brand A filter
            products_after_removal = len(driver.find_elements(By.CSS_SELECTOR, ".products .available"))

            # Validate the change in product count
            self.assertNotEqual(products_after_brand_a, products_after_removal)
            
            # Interact with the price slider
            price_slider = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'price-filter')]//input[@type='range']"))
            )
            
            # Example interaction with the slider - move it
            ActionChains(driver).click_and_hold(price_slider).move_by_offset(-30, 0).release().perform()
            time.sleep(2)  # Wait to see the change

            # Count products after price change
            products_after_price_change = len(driver.find_elements(By.CSS_SELECTOR, ".products .available"))

            # Verify the product count changed after the slider interaction
            self.assertNotEqual(products_after_removal, products_after_price_change)

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()