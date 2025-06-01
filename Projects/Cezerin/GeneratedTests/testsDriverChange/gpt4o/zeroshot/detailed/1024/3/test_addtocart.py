import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')
    
    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        # (Already opened in setUp)

        # Step 2: Click on product category (e.g., Category A)
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product (e.g., Product A)
        product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 5: Explicitly click the cart icon (shopping bag) to open the mini-cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        cart_icon.click()

        # Step 6: Wait for the mini-cart to become visible
        go_to_checkout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))

        # Step 7: Verify that the "GO TO CHECKOUT" button is present inside the cart
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present.")

if __name__ == "__main__":
    unittest.main()