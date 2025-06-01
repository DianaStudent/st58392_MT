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
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 1: Open home page (already done in setUp)

        # Step 2: Click on the menu button
        menu_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_thumbnail = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li a')))
        product_thumbnail.click()

        # Step 5: Select a size
        size_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="option-button"]')))
        size_button.click()

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Step 8: Verify the "GO TO CHECKOUT" button is present
        go_to_checkout_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="checkout-button"]')))
        if not go_to_checkout_button or not go_to_checkout_button.is_displayed():
            self.fail('GO TO CHECKOUT button is not present.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()