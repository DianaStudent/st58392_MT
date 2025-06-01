import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://example.com/category-a/product-a')  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        # Add product to cart
        try:
            add_to_cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart > button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Failed to add product to cart: " + str(e))

        # Click on the cart button (shopping bag)
        try:
            cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button .icon"))
            )
            cart_button.click()
        except Exception as e:
            self.fail("Failed to click on cart button: " + str(e))

        # Wait for the presence of "GO TO CHECKOUT" button in popup
        try:
            go_to_checkout_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-cart-open [href='/checkout']"))
            )
            assert go_to_checkout_button.is_displayed()
        except Exception as e:
            self.fail("GO TO CHECKOUT button not present: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()