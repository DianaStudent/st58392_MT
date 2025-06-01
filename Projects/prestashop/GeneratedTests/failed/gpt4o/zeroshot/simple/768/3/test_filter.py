from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        
    def test_product_filter(self):
        driver = self.driver
        
        # Navigate to Art category
        try:
            art_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_link.click()
        except Exception as e:
            self.fail("Art category link not found or not clickable: " + str(e))
        
        # Wait for filter sidebar
        try:
            filters_section = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except Exception as e:
            self.fail("Filter sidebar not found: " + str(e))

        # Get initial product count
        try:
            initial_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
            initial_count = len(initial_products)
        except Exception as e:
            self.fail("Unable to determine initial product count: " + str(e))

        # Select "Matt paper" filter
        try:
            matt_paper_filter = driver.find_element(By.XPATH, "//label[contains(., 'Matt paper')]")
            matt_paper_filter.click()
        except Exception as e:
            self.fail("Matt paper filter checkbox not found: " + str(e))
        
        # Wait for product count to change
        WebDriverWait(driver, 20).until(
            lambda x: len(x.find_elements(By.CSS_SELECTOR, ".product-miniature")) != initial_count
        )
        
        # Get filtered product count
        try:
            filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
            filtered_count = len(filtered_products)
        except Exception as e:
            self.fail("Unable to determine filtered product count: " + str(e))
        
        # Assertion to verify product count change
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filter applied")

        # Remove filter (reload page or uncheck filter, depending on site's behavior)
        driver.refresh()
        
        # Wait for products to reset
        WebDriverWait(driver, 20).until(
            lambda x: len(x.find_elements(By.CSS_SELECTOR, ".product-miniature")) == initial_count
        )

        # Get final product count
        try:
            final_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
            final_count = len(final_products)
        except Exception as e:
            self.fail("Unable to determine final product count: " + str(e))
        
        # Final assertion to verify removal of filter
        self.assertEqual(initial_count, final_count, "Product count did not reset after filter was removed")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()