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
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # 1. Open home page - already opened in setUp()

        # 2. Click on product category
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        if not category_link:
            self.fail("Category link not found.")
        category_link.click()

        # 3. Select the first product
        product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        if not product_link:
            self.fail("Product link not found.")
        product_link.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found or is empty.")
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        if not cart_button:
            self.fail("Cart button not found.")
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary")))
        if not checkout_button:
            self.fail("Checkout button not found or is empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()