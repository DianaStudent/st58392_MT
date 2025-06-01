from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
    
    def test_add_to_cart(self):
        driver = self.driver
        
        # Navigate to Category A
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except:
            self.fail("Category A link not found or clicked")
        
        # Navigate to Product A
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except:
            self.fail("Product A link not found or clicked")
        
        # Add to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to Cart button not found or clicked")
        
        # Click on the cart button (shopping bag)
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button img[alt='cart']"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found or clicked")
        
        # Wait for the presence of "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT"))
            )
        except:
            self.fail("GO TO CHECKOUT button not visible, test failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()