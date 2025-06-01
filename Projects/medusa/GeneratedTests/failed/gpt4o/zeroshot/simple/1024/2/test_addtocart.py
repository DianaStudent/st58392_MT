from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Go to Store
        store_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-store-link']"))
        )
        store_link.click()

        # Select product (Medusa Sweatshirt)
        product = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
        )
        product.click()

        # Select size
        size_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Add to cart
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Open cart
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Check for "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='checkout-button']"))
            )
        except:
            self.fail("GO TO CHECKOUT button not found.")

if __name__ == "__main__":
    unittest.main()