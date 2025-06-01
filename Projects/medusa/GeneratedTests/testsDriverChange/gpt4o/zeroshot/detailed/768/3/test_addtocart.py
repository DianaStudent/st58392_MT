from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on the first product image (Thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li:first-child img")))
        product_image.click()

        # Step 4: Select size by clicking the size button "L"
        size_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 5: Add the product to the cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if not add_to_cart_button.text == "Add to cart":
            self.fail("Add to cart button not enabled")
        add_to_cart_button.click()

        # Step 6: Explicitly click the cart button
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='checkout-button']")))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found")

if __name__ == "__main__":
    unittest.main()