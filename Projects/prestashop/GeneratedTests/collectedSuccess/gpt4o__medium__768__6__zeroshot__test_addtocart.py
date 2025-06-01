import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_add_to_cart_process(self):
        driver = self.driver
        
        try:
            # Step 2: Click on a product category
            category = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#category-9 a"))
            )
            category.click()
            
            # Step 3: Select the first product listed in the category
            product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-miniature:first-child .product-title a"))
            )
            product.click()
            
            # Step 4: On the product detail page, click the "Add to cart" button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
            )
            add_to_cart_button.click()
            
            # Step 5: Wait for the modal popup
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
            )
            
            # Step 6: Verify the modal contains the success message
            self.assertIn("successfully added to your shopping cart", modal_title.text)
        
        except Exception as e:
            self.fail(str(e))
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()