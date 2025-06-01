import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 20)

            # Open menu
            menu_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]'))
            )
            menu_button.click()

            # Click on "Store"
            store_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]'))
            )
            store_link.click()

            # Click on the first product
            first_product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li a'))
            )
            first_product.click()

            # Select size "L"
            size_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="option-button"]:nth-child(1)'))
            )
            size_button.click()

            # Add the product to cart
            add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]'))
            )
            add_to_cart_button.click()

            # Open cart
            cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]'))
            )
            cart_button.click()

            # Verify "Go to checkout" button is present
            go_to_checkout_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="checkout-button"]'))
            )
            self.assertIsNotNone(go_to_checkout_button, "Go to checkout button not found")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()