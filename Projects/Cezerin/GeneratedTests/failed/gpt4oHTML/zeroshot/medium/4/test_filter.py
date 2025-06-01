from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSeleniumFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_process(self):
        # Step 1: Open the category page
        self.driver.get("http://localhost:3000/category-a")
        
        # Step 2: Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='attribute-title' and text()='Brand']/following-sibling::label[input]/input")
        ))
        brand_a_checkbox.click()
        
        # Wait 2 seconds to allow UI update
        time.sleep(2)
        
        # Step 3: Verify the number of product cards changes (e.g., 2 → 1)
        products_displayed = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'products')]//div[@class='column']")
        ))
        self.assertEqual(len(products_displayed), 1, "Number of products after filter not as expected.")

        # Step 4: Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        
        # Wait 2 seconds to allow UI update
        time.sleep(2)

        # Verify the original number of product cards is restored (e.g., 1 → 2)
        products_displayed = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'products')]//div[@class='column']")
        ))
        self.assertEqual(len(products_displayed), 2, "Number of products after unchecking filter not as expected.")

        # Step 5: Locate the price slider component
        # Assuming a slider element exists in the form of two handles
        price_handle = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='price-filter']//div[@class='column']")
        ))

        # Step 6: Mimic moving the price slider (This is a placeholder, actual slider interaction might differ)
        # Here we will mimic a slider range adjustment using actions or keys for illustration; implementation depends on slider library
        # find the handle and move it, would vary based on actual slider implementation (could use ActionChains)
        # Placeholder method as there might be specifics for drag and drop or other JS function
        # Instructions would depend on how sliders are implemented on target pages, possibly with JS executions
        
        # Verify product count changes again
        # Placeholder to show asserting a change
        updated_products_displayed = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'products')]//div[@class='column']")
        ))
        # Assert that the product count changes from the previous state
        self.assertNotEqual(len(updated_products_displayed), 2, "Product count did not change after price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()