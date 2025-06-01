import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver

        # Click the menu button
        menu_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-menu-button"]'))
        )
        menu_button.click()

        # Click the "Store" link
        store_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="store-link"]'))
        )
        store_link.click()

        # Click on the first product image (Thumbnail)
        product_image = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-wrapper"] img'))
        )
        product_image.click()

        # Select the size 'L'
        size_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='option-button']:nth-child(1)"))
        )
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-product-button"]'))
        )
        add_to_cart_button.click()

        # Explicitly click the cart button
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-cart-link"]'))
        )
        cart_button.click()

        # Verify the "GO TO CHECKOUT" button is present
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="checkout-button"]'))
        )

        if not go_to_checkout_button or not go_to_checkout_button.is_displayed():
            self.fail('GO TO CHECKOUT button is not present or not visible')

if __name__ == "__main__":
    unittest.main()