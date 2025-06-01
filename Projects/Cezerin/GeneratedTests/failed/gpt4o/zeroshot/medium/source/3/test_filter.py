from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.url = "http://localhost:3000/category-a"
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def setUp(self):
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_brand_a_filter(self):
        # Wait for the page to load and find product cards
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-caption')))
        products_before = self.driver.find_elements(By.CLASS_NAME, 'product-caption')

        # Apply "Brand A" filter
        brand_a_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and following-sibling::text()='Brand A']"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Check filtered product list
        products_after_filter = self.driver.find_elements(By.CLASS_NAME, 'product-caption')
        self.assertNotEqual(len(products_before), len(products_after_filter),
                            "Product count should change after applying Brand A filter")
        
        # Uncheck "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Check if original number of products is restored
        products_after_unfilter = self.driver.find_elements(By.CLASS_NAME, 'product-caption')
        self.assertEqual(len(products_before), len(products_after_unfilter),
                         "Product count should be restored after unchecking Brand A filter")
    
    def test_apply_price_range_filter(self):
        # Locate slider elements (change these selectors to match your slider handles)
        # Assuming there are certain elements with class names that help move slider
        slider_handle = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']"))
        )
        
        # Check current number of product cards
        products_initial = self.driver.find_elements(By.CLASS_NAME, 'product-caption')

        # Move slider using ActionChains or JavaScript (replace with actual logic)
        # For demonstration, moving using JavaScript:
        self.driver.execute_script("arguments[0].style.left = '50%';", slider_handle)
        time.sleep(2)

        # Check if product count changes as expected
        products_after_slider = self.driver.find_elements(By.CLASS_NAME, 'product-caption')
        self.assertNotEqual(len(products_initial), len(products_after_slider),
                            "Product count should change after adjusting price slider")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()