from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        # Page is already opened in `setUp`

        # Step 2: Click on product category (Category A)
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product (Product A)
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon to open the mini-cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Step 6: Wait for the mini-cart to become visible
        goto_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered")))

        # Step 7: Verify that the "GO TO CHECKOUT" button is present inside the cart
        if not goto_checkout_button or goto_checkout_button.text != "GO TO CHECKOUT":
            self.fail("GO TO CHECKOUT button is not present in the mini-cart.")

if __name__ == "__main__":
    unittest.main()