import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the menu button ("Menu").
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Click the "Store" link.
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Click on the first product image (Thumbnail).
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li a')))
        product_image.click()

        # Select size by clicking the size button "L".
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="option-button" and text()="L"]')))
        size_button.click()

        # Add the product to the cart.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        if add_to_cart_button.text != "Add to cart":
            self.fail("Add to cart button is not available or not enabled")
        add_to_cart_button.click()

        # Click the cart button to open the cart.
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="checkout-button"]')))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()