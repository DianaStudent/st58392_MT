from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click the menu button ("Menu").
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (Thumbnail) - first product.
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-wrapper'] img")))
        first_product.click()

        # Step 4: Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 5: Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        self.assertIsNotNone(add_to_cart_button, "Add to cart button is missing")
        add_to_cart_button.click()

        # Step 6: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='checkout-button']")))
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()