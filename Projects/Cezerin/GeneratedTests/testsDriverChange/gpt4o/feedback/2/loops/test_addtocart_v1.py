from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 2: Click on product category (e.g. "/category-a")
        category_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href='/category-a']")))
        self.assertTrue(category_link, "Category link not found or is empty.")
        category_link.click()

        # Step 3: Select the first product (e.g. "/category-a/product-a")
        product_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        self.assertTrue(product_link, "Product link not found or is empty.")
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        self.assertTrue(add_to_cart_button, "'Add to cart' button not found or is empty.")
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "span.cart-button")))
        self.assertTrue(cart_button, "Cart button not found or is empty.")
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertTrue(go_to_checkout_button, "'GO TO CHECKOUT' button not found or is empty.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()