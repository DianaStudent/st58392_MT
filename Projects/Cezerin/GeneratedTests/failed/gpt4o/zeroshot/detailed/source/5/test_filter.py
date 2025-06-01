from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Wait for products and filters to be fully loaded
        products_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "section-category")))
        
        # Verify products are initially loaded
        product_cards = driver.find_elements(By.CLASS_NAME, "available")
        if not product_cards:
            self.fail("No product cards are initially loaded.")

        initial_product_count = len(product_cards)
        self.assertEqual(initial_product_count, 2, "Initial product count should be 2.")

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input")))
        brand_a_checkbox.click()
        
        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A filter should be checked.")
        
        # Wait for filtered results
        self.driver.implicitly_wait(2)
        filtered_product_cards = driver.find_elements(By.CLASS_NAME, "available")
        self.assertEqual(len(filtered_product_cards), 1, "Filtered product count should be 1 after applying Brand A filter.")

        # Uncheck the filter
        brand_a_checkbox.click()
        
        # Confirm product count is restored
        self.driver.implicitly_wait(2)
        restored_product_cards = driver.find_elements(By.CLASS_NAME, "available")
        self.assertEqual(len(restored_product_cards), 2, "Product count should be restored to 2 after removing Brand A filter.")

        # Locate the price slider component and adjust the right handle
        price_slider = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']//input[@type='range' and @aria-valuenow='1250']")))
        
        # Move price slider handle
        action = webdriver.ActionChains(driver)
        action.click_and_hold(price_slider).move_by_offset(-50, 0).release().perform()

        # Wait for filtered results
        self.driver.implicitly_wait(2)
        price_filtered_product_cards = driver.find_elements(By.CLASS_NAME, "available")
        self.assertEqual(len(price_filtered_product_cards), 1, "Product count should be 1 after adjusting price slider to 1159.")

if __name__ == "__main__":
    unittest.main()