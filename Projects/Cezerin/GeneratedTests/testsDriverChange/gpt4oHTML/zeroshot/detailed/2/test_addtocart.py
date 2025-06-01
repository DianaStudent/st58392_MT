import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(20)
        self.driver.get("data:text/html;charset=utf-8," + html_data['home_page'])

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        # Already done in setUp()

        # Step 2: Click on product category (e.g., Category A)
        category_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
        category_a_link.click()

        # Step 3: Select the first product (e.g., Product A)
        product_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]')))
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.button-addtocart > button')))
        add_to_cart_button.click()

        # Step 5: Explicitly click the cart icon (shopping bag) to open the mini-cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.cart-button')))
        cart_button.click()

        # Step 6: Wait for the mini-cart to become visible
        mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.mini-cart-open')))

        # Step 7: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.button.is-primary.is-fullwidth')))
        if not go_to_checkout_button:
            self.fail('GO TO CHECKOUT button is not present in the mini-cart.')

if __name__ == "__main__":
    unittest.main()