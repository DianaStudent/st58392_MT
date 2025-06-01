import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_filters(self):
        driver = self.driver
        
        # Wait for Brand A checkbox and apply the filter
        try:
            brand_a_checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[input[@type='checkbox' and following-sibling::text()[contains(., 'Brand A')]]]")))
            self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox not found")
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to find or click Brand A checkbox: {str(e)}")

        time.sleep(2)  # Wait for UI update

        # Verify number of visible product cards is 1
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products), 1, "Expected 1 product after filtering by Brand A")
        except Exception as e:
            self.fail(f"Failed to locate product cards: {str(e)}")

        # Uncheck the Brand A filter
        try:
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to uncheck Brand A filter: {str(e)}")

        time.sleep(2)  # Wait for UI update

        # Verify number of visible product cards is restored to 2
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products), 2, "Expected 2 products after unchecking Brand A filter")
        except Exception as e:
            self.fail(f"Failed to locate product cards after unchecking: {str(e)}")

        # Locate and move the price slider
        try:
            price_slider = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-filter-values")))
            self.assertIsNotNone(price_slider, "Price slider not found")
            slider_handle = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[contains(@style,'left')]")))
            self.assertIsNotNone(slider_handle, "Slider handle not found")
            # Move the slider handle
            action = ActionChains(driver)
            action.click_and_hold(slider_handle).move_by_offset(-20, 0).release().perform()
        except Exception as e:
            self.fail(f"Failed to move the price slider: {str(e)}")

        time.sleep(2)  # Wait for UI update

        # Verify that the product count changes again
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
            self.assertEqual(len(products), 1, "Expected product count change after applying price filter")
        except Exception as e:
            self.fail(f"Failed to locate product cards after price filter: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()