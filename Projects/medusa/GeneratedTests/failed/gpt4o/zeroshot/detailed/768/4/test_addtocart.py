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

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open home page
        self.assertIn("Ecommerce Starter Template", driver.page_source)

        # Click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="nav-menu-button"]')))
        menu_button.click()

        # Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="store-link"]')))
        store_link.click()

        # Click on a product image (Thumbnail) - first product
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="products-list"]/li[1]/a/div')))
        first_product.click()

        # Select size "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="product-options"]/button[text()="L"]')))
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="add-product-button" and text()="Add to cart"]')))
        add_to_cart_button.click()

        # Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="nav-cart-link"]')))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="checkout-button"]')))
            self.assertIsNotNone(go_to_checkout_button)
        except:
            self.fail("GO TO CHECKOUT button is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()