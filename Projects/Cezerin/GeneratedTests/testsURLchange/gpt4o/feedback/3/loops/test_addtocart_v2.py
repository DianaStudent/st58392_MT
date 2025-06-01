from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on product category (Category A)
        category_a_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        category_a_link.click()

        # Step 3: Select the first product (Product A)
        product_a_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.is-success.is-fullwidth'))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.cart-button img[title="cart"]'))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.button.is-primary.is-fullwidth.has-text-centered[href="/checkout"]'))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button not found in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()