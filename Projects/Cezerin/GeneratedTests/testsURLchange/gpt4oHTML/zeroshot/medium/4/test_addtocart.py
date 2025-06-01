import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/") # Replace with your local test server URL

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        # (Already done in setUp method)
        
        # Step 2: Click on product category
        try:
            category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_link.click()
        except Exception:
            self.fail("Category link '/category-a' not found or not clickable")

        # Step 3: Select the first product
        try:
            product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_link.click()
        except Exception:
            self.fail("Product link '/category-a/product-a' not found or not clickable")

        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button")))
            add_to_cart_button.click()
        except Exception:
            self.fail("Add to cart button not found or not clickable")

        # Step 5: Click the cart icon/button to open the shopping bag
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-block-right .cart-button")))
            cart_button.click()
        except Exception:
            self.fail("Cart button (shopping bag icon) not found or not clickable")

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered[href='/checkout']")))
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        except Exception:
            self.fail("GO TO CHECKOUT button not found in cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()