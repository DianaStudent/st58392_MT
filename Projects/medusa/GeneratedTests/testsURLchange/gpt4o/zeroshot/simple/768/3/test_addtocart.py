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
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to the store page
        store_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-store-link']")))
        store_link.click()

        # Click on a product
        product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product.click()

        # Select the size
        size_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        # Add to cart button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button.text == "Add to cart":
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button is not available")

        # Click on cart icon
        cart_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_link.click()

        # Verify presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']")))
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()