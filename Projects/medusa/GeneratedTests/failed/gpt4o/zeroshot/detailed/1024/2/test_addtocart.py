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

        # 1. Open home page - Already done in setUp

        # 2. Click the menu button ("Menu").
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="nav-menu-button"]')))
        if not menu_button:
            self.fail("Menu button not found")
        menu_button.click()

        # 3. Click the "Store" link.
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="store-link"]')))
        if not store_link:
            self.fail("Store link not found")
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product.
        product_image = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-wrapper"] img')))
        if not product_image:
            self.fail("Product image not found")
        product_image.click()

        # 5. Select size by clicking the size button "L".
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        if not size_button:
            self.fail("Size button 'L' not found")
        size_button.click()

        # 6. Add the product to the cart.
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-product-button"]')))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart.
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="nav-cart-link"]')))
        if not cart_button:
            self.fail("Cart button not found")
        cart_button.click()

        # 8. Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="checkout-button"]')))
        if not go_to_checkout_button:
            self.fail("Go to checkout button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()