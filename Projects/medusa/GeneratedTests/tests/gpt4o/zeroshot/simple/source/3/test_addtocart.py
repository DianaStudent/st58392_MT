import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to the store page
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-store-link']"))
            )
            store_link.click()
        except Exception:
            self.fail("Failed to find or click store link.")

        # Click on the first product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except Exception:
            self.fail("Failed to find or click product link.")

        # Select size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='L']"))
            )
            size_button.click()
        except Exception:
            self.fail("Failed to find or click size button.")

        # Add to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except Exception:
            self.fail("Failed to find or click add to cart button.")

        # Open cart and check for checkout button
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
            )
            cart_link.click()
        except Exception:
            self.fail("Failed to find or click cart link.")

        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']"))
            )
        except Exception:
            self.fail("Checkout button not present in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()