from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Open home page, category A
        category_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_link.click()

        # Select the first product
        product_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )
        add_to_cart_button.click()

        # Click the cart button (shopping bag) explicitly
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button"))
        )
        cart_button.click()
        
        # Wait for the mini-cart to become visible
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout'].button.is-primary.is-fullwidth"))
        )
        
        # Verify the "GO TO CHECKOUT" button is present inside the cart
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found in the mini-cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()