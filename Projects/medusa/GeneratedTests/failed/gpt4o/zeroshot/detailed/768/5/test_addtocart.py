from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 2: Click the menu button
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Step 3: Click the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Step 4: Click on the product image (Thumbnail) - first product
        first_product_image = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li:first-child img')))
        first_product_image.click()

        # Step 5: Select size by clicking the size button "L"
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]')))
        size_button.click()

        # Step 6: Add the product to the cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="checkout-button"]')))
        self.assertIsNotNone(go_to_checkout_button)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()