from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to the store using the menu
        try:
            menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
            menu_button.click()
            
            store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
            store_link.click()
        except Exception as e:
            self.fail(f"Navigation to store failed: {e}")

        # Select a product
        try:
            product_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]')))
            product_link.click()
        except Exception as e:
            self.fail(f"Selecting product failed: {e}")

        # Select size
        try:
            size_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="option-button"]')))
            size_button.click()
        except Exception as e:
            self.fail(f"Selecting size failed: {e}")

        # Add to cart
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding to cart failed: {e}")

        # Go to cart
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
            cart_button.click()
            
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="checkout-button"]')))
            # If present, test is successful
        except Exception as e:
            self.fail(f"Checkout button not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()