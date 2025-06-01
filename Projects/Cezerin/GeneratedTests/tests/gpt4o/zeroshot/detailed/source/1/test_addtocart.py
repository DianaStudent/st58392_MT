import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Step 2: Click on Category A
            category_a = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            self.assertIsNotNone(category_a, "Category A not found")
            category_a.click()

            # Step 3: Select the first product (Product A)
            product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            self.assertIsNotNone(product, "Product A not found")
            product.click()

            # Step 4: Click "Add to cart"
            add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button"))
            )
            self.assertIsNotNone(add_to_cart_button, "Add to cart button not found")
            add_to_cart_button.click()

            # Step 5: Click on the cart icon
            cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
            )
            self.assertIsNotNone(cart_button, "Cart button not found")
            cart_button.click()
            
            # Step 6: Wait for the mini-cart to become visible
            go_to_checkout_button = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found")
            
        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()