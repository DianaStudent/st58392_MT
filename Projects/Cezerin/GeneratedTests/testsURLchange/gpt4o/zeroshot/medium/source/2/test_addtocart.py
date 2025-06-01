import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Open home page and click on product category
        category_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.primary-nav a[href="/category-a"]')
        ))
        self.assertIsNotNone(category_link)
        category_link.click()

        # Select the first product
        product_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.products a[href="/category-a/product-a"]')
        ))
        self.assertIsNotNone(product_link)
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.button-addtocart .button')
        ))
        self.assertIsNotNone(add_to_cart_button)
        add_to_cart_button.click()

        # Click on the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.cart-button')
        ))
        self.assertIsNotNone(cart_button)
        cart_button.click()

        # Verify the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.mini-cart-open a[href="/checkout"]')
        ))
        self.assertIsNotNone(checkout_button)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()