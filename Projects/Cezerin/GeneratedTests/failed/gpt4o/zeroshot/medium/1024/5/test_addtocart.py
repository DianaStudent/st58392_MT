from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        # Verify home page loaded by checking for a specific element
        home_category_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary-nav .has-items .cat-parent a[href="/category-a"]')))
        
        # Step 2: Click on product category
        home_category_a.click()

        # Step 3: Select the first product
        first_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.products a[href="/category-a/product-a"]')))
        first_product.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart .button.is-success')))
        add_to_cart_btn.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button img[alt="cart"]')))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mini-cart-open .button[href="/checkout"]')))
        if not go_to_checkout_btn:
            self.fail("GO TO CHECKOUT button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()