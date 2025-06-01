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

        # Navigate to Category A
        try:
            category_a = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
            category_a.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Category A: {e}")

        # Select Product A
        try:
            product_a = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_a.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Product A page: {e}")

        # Add Product A to Cart
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add Product A to cart: {e}")

        # Click on the cart button
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button img[alt='cart']")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to open cart: {e}")

        # Verify presence of "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button.is-primary.is-fullwidth")))
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()