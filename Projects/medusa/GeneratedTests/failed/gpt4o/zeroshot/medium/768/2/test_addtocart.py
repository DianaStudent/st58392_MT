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
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (thumbnail)
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] > li:nth-child(1) > a > div img")))
        product_image.click()

        # Step 4: Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'L')]")))
        size_button.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if not add_to_cart_button or not add_to_cart_button.is_displayed():
            self.fail("Add to Cart button not found or not visible")
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='checkout-button']")))
        if not go_to_checkout_button or not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()