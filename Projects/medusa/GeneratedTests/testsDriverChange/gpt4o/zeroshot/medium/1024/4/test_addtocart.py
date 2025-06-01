from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
    
    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1 - Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2 - Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3 - Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='product-wrapper'] img")))
        if product_image is None:
            self.fail("Product image not found.")
        product_image.click()

        # Step 4 - Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 5 - Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button is None:
            self.fail("Add to Cart button not found.")
        add_to_cart_button.click()

        # Step 6 - Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7 - Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']")))
        if go_to_checkout_button is None:
            self.fail("GO TO CHECKOUT button not found.")
        
        # Ensure button is not empty
        go_to_checkout_text = go_to_checkout_button.text
        if not go_to_checkout_text:
            self.fail("GO TO CHECKOUT button is empty.")
        
        # Assertion to confirm test flow is complete
        self.assertTrue(True, "Tested successfully!")

if __name__ == "__main__":
    unittest.main()