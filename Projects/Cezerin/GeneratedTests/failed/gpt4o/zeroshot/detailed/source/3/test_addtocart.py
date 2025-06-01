from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Step 2: Click on product category (Category A)
            category_a_link = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            category_a_link.click()

            # Step 3: Select the first product (Product A)
            product_a_link = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_a_link.click()

            # Step 4: Click the "Add to cart" button
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()

            # Step 5: Click the cart icon (shopping bag)
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button"))
            )
            cart_button.click()

            # Step 6: Wait for the mini-cart to become visible
            go_to_checkout_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered"))
            )
            
            # Step 7: Verify that the "GO TO CHECKOUT" button is present
            self.assertIsNotNone(go_to_checkout_button, "The 'GO TO CHECKOUT' button is not present.")

        except Exception as e:
            self.fail(f"Test failed with exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()