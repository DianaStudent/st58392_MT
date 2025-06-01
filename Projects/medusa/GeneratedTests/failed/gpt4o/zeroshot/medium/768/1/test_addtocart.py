from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page - already done in setUp()

        # 2. Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (thumbnail)
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] a[href='/dk/products/sweatshirt'] img")))
        product_image.click()

        # 5. Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']:nth-child(1)")))
        size_button.click()

        # 6. Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # 8. Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
        
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present.")

        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")

if __name__ == "__main__":
    unittest.main()