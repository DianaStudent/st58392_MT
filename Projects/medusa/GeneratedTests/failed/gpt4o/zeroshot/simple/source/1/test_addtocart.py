from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Click on 'Store' link in nav menu
        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-store-link']")))
        store_link.click()

        # Click on 'Medusa Sweatshirt' product link
        product_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product_link.click()

        # Select product size 'L'
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Click 'Add to cart' button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Click on 'Cart' link in nav menu
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_link.click()

        # Wait for 'GO TO CHECKOUT' button
        try:
            go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='checkout-button']")))
            self.assertIsNotNone(go_to_checkout_button, "Go to checkout button should be present.")
        except:
            self.fail("Failed to find 'GO TO CHECKOUT' button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()