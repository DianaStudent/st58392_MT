import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        try:
            # Step 2: Click on product category (e.g., Category A)
            category_a = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            category_a.click()

            # Step 3: Select the first product (e.g., Product A)
            product_a = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_a.click()

            # Step 4: Click the "Add to cart" button
            add_to_cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button"))
            )
            add_to_cart_button.click()

            # Step 5: Explicitly click the cart icon (shopping bag) to open the mini-cart
            cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
            )
            cart_button.click()

            # Step 6: Wait for mini-cart to become visible
            go_to_checkout_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
            )

            # Step 7: Verify that the "GO TO CHECKOUT" button is present inside the cart
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found in mini-cart")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

if __name__ == "__main__":
    unittest.main()