import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8000/dk')
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Click on the menu button
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (thumbnail)
        product_thumbnail = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-wrapper'] img")))
        product_thumbnail.click()

        # Step 4: Select a size
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        if not size_button.text.strip():
            self.fail("Size button text is empty.")
        size_button.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        if not add_to_cart_button.text.strip():
            self.fail("Add to Cart button text is empty.")
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='checkout-button']")))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()