from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Click on the Store menu
        try:
            store_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-store-link']")))
            store_link.click()
        except:
            self.fail("Store link not found")

        # Click on the product
        try:
            product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
            product_link.click()
        except:
            self.fail("Product link not found")

        # Select size
        try:
            size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
            size_button.click()
        except:
            self.fail("Size selection not found")

        # Add to cart
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Click on Cart button
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Verify Go to checkout button presence
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        except:
            self.fail("Go to checkout button not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()