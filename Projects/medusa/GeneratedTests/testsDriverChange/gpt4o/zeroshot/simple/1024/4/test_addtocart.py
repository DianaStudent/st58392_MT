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
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to "Store" using the nav-store-link
        try:
            store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-store-link"]')))
            store_link.click()
        except:
            self.fail("Store link not found.")

        # Click on the product link for "Medusa Sweatshirt"
        try:
            product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]')))
            product_link.click()
        except:
            self.fail("Product link not found.")

        # Select a size (e.g., 'L')
        try:
            size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
            size_button.click()
        except:
            self.fail("Size option 'L' not found.")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or product might be out of stock.")

        # Click on the cart button
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
            cart_button.click()
        except:
            self.fail("Cart button not found.")

        # Wait for presence of "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="checkout-button"]')))
        except:
            self.fail("'GO TO CHECKOUT' button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()