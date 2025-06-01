import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on product category "Category A"
        category_a_selector = (By.CSS_SELECTOR, ".nav-level-0 .has-items .cat-parent a[href='/category-a']")
        category_a_element = wait.until(EC.presence_of_element_located(category_a_selector))
        category_a_element.click()

        # Select the first product "Product A"
        product_a_selector = (By.CSS_SELECTOR, "a[href='/category-a/product-a']")
        product_a_element = wait.until(EC.presence_of_element_located(product_a_selector))
        product_a_element.click()

        # Click the "Add to cart" button
        add_to_cart_button_selector = (By.CSS_SELECTOR, ".button-addtocart .button.is-success")
        add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_button_selector))
        add_to_cart_button.click()

        # Click the cart icon
        cart_button_selector = (By.CSS_SELECTOR, ".cart-button")
        cart_button = wait.until(EC.presence_of_element_located(cart_button_selector))
        cart_button.click()

        # Wait for the mini-cart to become visible
        go_to_checkout_button_selector = (By.CSS_SELECTOR, ".mini-cart-open .button.is-primary")
        go_to_checkout_button = wait.until(EC.presence_of_element_located(go_to_checkout_button_selector))
        
        # Verify that the "GO TO CHECKOUT" button is present and visible
        is_visible = EC.visibility_of(go_to_checkout_button)
        if not go_to_checkout_button or not is_visible(go_to_checkout_button):
            self.fail("GO TO CHECKOUT button is not present or visible in the mini-cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()