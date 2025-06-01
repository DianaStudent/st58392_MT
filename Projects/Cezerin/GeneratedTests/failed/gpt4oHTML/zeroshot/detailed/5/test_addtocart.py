from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCartProcess(unittest.TestCase):
    
    def setUp(self):
        # Setup Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:3000/"  # Replace with the actual URL of the home page
    
    def test_add_to_cart_process(self):
        driver = self.driver
        
        try:
            # Step 1: Open home page
            driver.get(self.base_url)
            
            # Step 2: Click on product category (e.g., Category A)
            category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
            )
            self.assertTrue(category_link.is_displayed() and category_link.is_enabled())
            category_link.click()
            
            # Step 3: Select the first product (e.g., Product A)
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            self.assertTrue(product_link.is_displayed() and product_link.is_enabled())
            product_link.click()
            
            # Step 4: Click the "Add to cart" button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            self.assertTrue(add_to_cart_button.is_displayed() and add_to_cart_button.is_enabled())
            add_to_cart_button.click()
            
            # Step 5: Explicitly click the cart icon (shopping bag)
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-block-right .cart-button img[alt='cart']"))
            )
            self.assertTrue(cart_icon.is_displayed() and cart_icon.is_enabled())
            cart_icon.click()
            
            # Step 6: Wait for the mini-cart to become visible
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/checkout') and contains(text(), 'Go to checkout')]"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed())
        
        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")
    
    def tearDown(self):
        # Close the browser once the test is completed
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()