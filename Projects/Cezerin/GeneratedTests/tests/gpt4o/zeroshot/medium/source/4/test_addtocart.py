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
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver

        # 1. Open home page
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
            ).click()
        except Exception as e:
            self.fail(f"Unable to click on Category A: {e}")

        # 2. Click on product category
        try:
            product_a = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            if not product_a:
                self.fail("Product A link is missing.")
            product_a.click()
        except Exception as e:
            self.fail(f"Unable to click on Product A: {e}")

        # 3. Select the first product and click "Add to cart"
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
            )
            if not add_to_cart_button:
                self.fail("Add to cart button is missing.")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Unable to click Add to cart: {e}")

        # 4. Click the cart icon/button to open the shopping bag
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button"))
            )
            if not cart_button:
                self.fail("Cart button is missing.")
            cart_button.click()
        except Exception as e:
            self.fail(f"Unable to click on cart button: {e}")

        # 5. Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
            if not go_to_checkout_button:
                self.fail("GO TO CHECKOUT button is missing.")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button is not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()