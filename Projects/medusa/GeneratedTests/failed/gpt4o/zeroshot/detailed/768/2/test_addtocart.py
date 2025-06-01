from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 1: Open home page - Already opened in setUp

        # Step 2: Click the menu button
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        if not menu_button:
            self.fail("Menu button not found")
        menu_button.click()

        # Step 3: Click the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        if not store_link:
            self.fail("'Store' link not found")
        store_link.click()

        # Step 4: Click on a product image - first product
        first_product_image = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='products-list'] a")))
        if not first_product_image:
            self.fail("First product image not found")
        first_product_image.click()

        # Step 5: Select size by clicking the size button "L"
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        if not size_button:
            self.fail("Size 'L' button not found")
        size_button.click()

        # Step 6: Add the product to the cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        if not cart_button:
            self.fail("Cart button not found")
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='checkout-button']")))
        if not go_to_checkout_button:
            self.fail("Go to checkout button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()