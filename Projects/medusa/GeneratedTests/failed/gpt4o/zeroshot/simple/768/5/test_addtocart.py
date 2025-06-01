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

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to the store page from the menu
        menu_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        store_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Select a product
        product_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product_link.click()

        # Select size
        size_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Click on cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Check for "GO TO CHECKOUT"
        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
        except:
            self.fail("Failed to find the GO TO CHECKOUT button")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()