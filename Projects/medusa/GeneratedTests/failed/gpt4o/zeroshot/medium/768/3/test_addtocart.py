from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_cart(self):
        # Step 1: Open home page
        self.assertTrue(self.driver.current_url.endswith("/dk"), "Failed to open the home page")

        # Step 2: Click on the menu button
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="product-wrapper"] img')))
        product_image.click()

        # Step 5: Select a size
        size_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="option-button"]')))
        size_button.click()

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        add_to_cart_text = add_to_cart_button.text.strip()
        if add_to_cart_text != "Add to cart":
            self.fail("Add to Cart button not available")
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')))
        go_to_checkout_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')

        if not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button is not present.")

if __name__ == "__main__":
    unittest.main()