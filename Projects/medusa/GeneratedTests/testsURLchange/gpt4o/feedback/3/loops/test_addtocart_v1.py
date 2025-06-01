import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click the menu button
        menu_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Click the store link
        store_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        store_link.click()

        # Click on the first product image (Thumbnail)
        first_product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] a"))
        )
        first_product.click()

        # Select size "L"
        size_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        self.assertEqual(add_to_cart_button.text, "Add to cart", "Add to cart button is not enabled.")
        add_to_cart_button.click()

        # Click the cart button
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']"))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")

if __name__ == "__main__":
    unittest.main()