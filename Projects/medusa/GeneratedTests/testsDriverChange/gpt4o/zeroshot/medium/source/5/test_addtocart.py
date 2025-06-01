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

    def test_add_to_cart(self):
        driver = self.driver

        # Wait for home page and click menu button
        menu_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Click on the "Store" link
        store_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        store_link.click()

        # Click on product image
        product_image = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] a"))
        )
        product_image.click()

        # Select a size
        size_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Click "Add to Cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Click the cart button
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Verify presence of "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']"))
        )
        
        if not go_to_checkout_button or not go_to_checkout_button.is_displayed():
            self.fail("Checkout button not found on the cart page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()