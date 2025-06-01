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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click on product category (Category A)
        try:
            category_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
            category_a.click()
        except:
            self.fail("Category A link is missing or not clickable")
        
        # Step 3: Select the first product (Product A)
        try:
            product_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]')))
            product_a.click()
        except:
            self.fail("Product A link is missing or not clickable")

        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-addtocart button')))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button is missing or not clickable")

        # Step 5: Click the cart icon to open the mini-cart
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button')))
            cart_button.click()
        except:
            self.fail("Cart button is missing or not clickable")
        
        # Step 6: Wait for the mini-cart to become visible
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]')))
        except:
            self.fail("GO TO CHECKOUT button is missing in the mini-cart")

        # Step 7: Verify GO TO CHECKOUT button is present
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found")

if __name__ == "__main__":
    unittest.main()