import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Find and click on the "Product A" link on the home page
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()

            # Find and click the "Add to cart" button on the product page
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()

            # Find and click the cart button (shopping bag icon)
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button img[alt='cart']"))
            )
            cart_button.click()

            # Wait for the "GO TO CHECKOUT" button to be present in the mini-cart
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed")

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()