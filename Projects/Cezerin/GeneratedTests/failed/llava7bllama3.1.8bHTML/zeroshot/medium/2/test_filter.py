from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFiltering(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")  # Replace with your HTML data URL or path

    def tearDown(self):
        self.driver.quit()

    def test_filter_products_by_brand_and_price(self):
        # Step 1: Open the category page
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#brand"))
        )

        # Step 2: Locate and apply the "Brand A" checkbox filter
        brand_filter = self.driver.find_element(By.CSS_SELECTOR, "input[title='Brand A']")
        brand_filter.click()

        # Wait for UI to update
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".available"))
        )

        # Step 3: Verify that the number of displayed product cards changes
        initial_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertGreater(initial_product_count, 0)

        # Apply filter again to ensure change
        brand_filter.click()

        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".available"))
        )

        updated_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertLess(updated_product_count, initial_product_count)

        # Step 4: Uncheck the "Brand A" filter
        brand_filter.click()

        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".available"))
        )

        # Step 5: Verify that the original number of product cards is restored
        self.assertEqual(updated_product_count, initial_product_count)

        # Step 6: Locate the price slider component
        price_slider = self.driver.find_element(By.CSS_SELECTOR, "div.slider")

        # Step 7: Move one of the slider handles to apply a price range filter
        handle = price_slider.find_element(By.XPATH, "//input[@type='range']")
        handle.send_keys("1000")  # Change value as per your requirement

        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".available"))
        )

        # Step 8: Verify that the product count changes again
        updated_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertLess(updated_product_count, initial_product_count)

if __name__ == "__main__":
    unittest.main()