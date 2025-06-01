from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.url = "http://localhost:3000/"
    
    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Open home page
        # (URL already opened in setUp)

        # 2. Click on product category
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary-nav a[href="/category-a"]'))
            )
            category_link.click()
        except:
            self.fail("Category A link not found or click failed.")

        # 3. Select the first product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
            )
            product_link.click()
        except:
            self.fail("Product A link not found or click failed.")

        # 4. Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to Cart button not found or click failed.")

        # 5. Click the cart icon to open the mini-cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button'))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found or click failed.")

        # 6. Wait for the mini-cart to become visible
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.button.is-primary.is-fullwidth'))
            )
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present.")
        except:
            self.fail("GO TO CHECKOUT button not found in mini-cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()