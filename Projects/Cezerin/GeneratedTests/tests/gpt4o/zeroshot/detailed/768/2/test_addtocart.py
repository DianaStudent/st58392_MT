import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        self.assertTrue(driver.title != "", "Home page did not load correctly")

        # Step 2: Click on product category (Category A)
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product (Product A)
        product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success")))
        add_to_cart_button.click()

        # Step 5: Explicitly click the cart icon (shopping bag) to open the mini-cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Step 6: Wait for the mini-cart to become visible
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        visible_check = EC.visibility_of(go_to_checkout_button)
        
        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        if not go_to_checkout_button or not visible_check(driver):
            self.fail("GO TO CHECKOUT button is not present inside the cart")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()