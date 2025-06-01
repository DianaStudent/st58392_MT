from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:3000/")  # Load the homepage HTML file locally
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Navigate to Category A Page
        try:
            category_a_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Category A'))
            )
            category_a_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Category A page: {e}")

        # Verify the page loaded is the Category A HTML content
        self.assertIn("Category A", driver.page_source)

        # Step 2: Click on a Product A
        try:
            product_a_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Product A'))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Product A page: {e}")

        # Verify the page loaded is the Product A HTML content
        self.assertIn("Product A", driver.page_source)

        # Step 3: Add Product A to Cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.is-success.is-fullwidth'))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add Product A to cart: {e}")

        # Step 4: Click on Cart Button (Shopping Bag Icon)
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.cart-button > img[title="cart"]'))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to open cart: {e}")

        # Step 5: Verify presence of "GO TO CHECKOUT" button (success criteria)
        try:
            go_to_checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Go to checkout'))
            )
        except Exception as e:
            self.fail(f"Checkout button not found: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()