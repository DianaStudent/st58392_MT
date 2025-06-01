from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        # Already done in setUp (driver.get)

        # Step 2: Click the menu button ("Menu")
        menu_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]'))
        )
        self.assertIsNotNone(menu_button, "Menu button is not present.")
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]'))
        )
        self.assertIsNotNone(store_link, "Store link is not present.")
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product
        first_product_image = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li:first-child img'))
        )
        self.assertIsNotNone(first_product_image, "First product image is not present.")
        first_product_image.click()

        # Step 5: Select size by clicking the size button "L"
        size_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="product-options"] button:nth-child(1)'))
        )
        self.assertIsNotNone(size_button, "Size button L is not present.")
        size_button.click()

        # Step 6: Add the product to the cart
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]'))
        )
        self.assertIsNotNone(add_to_cart_button, "Add to cart button is not present.")
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]'))
        )
        self.assertIsNotNone(cart_button, "Cart button is not present.")
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="checkout-button"]'))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()