from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Find and click the store link
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-store-link"]'))
            )
            store_link.click()

            # Find and click the first product link (Medusa Sweatshirt)
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]'))
            )
            product_link.click()

            # Select a size (L)
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]'))
            )
            size_button.click()

            # Find and click the add to cart button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]'))
            )
            add_to_cart_button.click()

            # Find and click the cart link
            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="headlessui-popover-button-:Rrmdtt7:"] > a[data-testid="nav-cart-link"]'))
            )
            cart_link.click()

            # Wait for the "GO TO CHECKOUT" button to be present
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="checkout-button"] > button'))
            )

            # If the button is present, the test is successful
            self.assertTrue(go_to_checkout_button.is_displayed())

        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()