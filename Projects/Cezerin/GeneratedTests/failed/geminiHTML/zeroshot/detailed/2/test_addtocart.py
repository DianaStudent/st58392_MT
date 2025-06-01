import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page (already done in setUp)

        # 2. Click on product category (Category A)
        category_a_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found")

        # 3. Select the first product (Product A)
        product_a_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found")

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 5. Explicitly click the cart icon (shopping bag)
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found")

        # 6. Wait for the mini-cart to become visible.
        mini_cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mini-cart-open")))
        if not mini_cart:
            self.fail("Mini cart did not become visible")

        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/checkout') and contains(text(), 'Go to checkout')]")))
        if not go_to_checkout_button:
            self.fail("Go to checkout button not found in mini cart")

if __name__ == "__main__":
    unittest.main()