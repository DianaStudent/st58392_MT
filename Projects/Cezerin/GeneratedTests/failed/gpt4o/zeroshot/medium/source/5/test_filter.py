from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_filters(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input")))
        if not brand_a_checkbox:
            self.fail("Brand A checkbox not found or empty")
        
        # Click the checkbox to apply filter
        brand_a_checkbox.click()
        time.sleep(2)  # Allow UI to update

        # Step 3: Verify that the number of displayed product cards changes
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        filtered_count = len(product_cards)
        self.assertEqual(filtered_count, 1, "Product count should change to 1 after applying Brand A filter")

        # Step 4: Uncheck the "Brand A" filter.
        brand_a_checkbox.click()
        time.sleep(2)  # Allow UI to update

        # Verify that the original number of product cards is restored
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        restored_count = len(product_cards)
        self.assertEqual(restored_count, 2, "Product count should restore to 2 after removing Brand A filter")

        # Step 5: Locate the price slider component.
        price_slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@has-text-left='$950.00']")))
        if not price_slider:
            self.fail("Price slider not found or empty")
        
        # Move one of the slider handles to apply a price range filter
        slider_handle = driver.find_element(By.XPATH, "//div[@class='price-filter']//div[contains(@class, 'has-text-left')]")
        
        # Perform drag-and-drop operation (assumes the slider handle can be moved)
        ActionChains(driver).click_and_hold(slider_handle).move_by_offset(10, 0).release().perform()
        time.sleep(2)  # Allow UI to update

        # Verify that the product count changes again
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        price_filtered_count = len(product_cards)
        self.assertEqual(price_filtered_count, 1, "Product count should change after applying price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()