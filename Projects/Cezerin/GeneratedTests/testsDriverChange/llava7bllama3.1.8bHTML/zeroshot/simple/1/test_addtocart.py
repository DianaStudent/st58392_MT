import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.get("data:text/html," + html_data)

        # Wait for Add to Cart button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )

        if not add_to_cart_button:
            self.fail("Add to cart button is missing")

        # Click Add to Cart button
        add_to_cart_button.click()

        # Wait for Cart button
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-cart-button"))
        )

        if not cart_button:
            self.fail("Cart button is missing")

        # Click Cart button
        cart_button.click()

        # Wait for GO TO CHECKOUT button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )

if __name__ == "__main__":
    unittest.main()