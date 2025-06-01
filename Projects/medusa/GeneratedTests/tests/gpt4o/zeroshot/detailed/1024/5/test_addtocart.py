from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Click on the product image (first product)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="Thumbnail"]')))
        product_image.click()

        # Select size "L"
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="L"]')))
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        if add_to_cart_button.text != "Add to cart":
            self.fail("Add to cart button not clickable or not found.")
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')))
        if not checkout_button.text or checkout_button.text != "Go to cart":
            self.fail("Go to checkout button not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()