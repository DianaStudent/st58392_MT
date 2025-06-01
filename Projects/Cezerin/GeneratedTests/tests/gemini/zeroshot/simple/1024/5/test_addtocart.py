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
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A page
        try:
            category_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except Exception as e:
            self.fail(f"Failed to click Category A link: {e}")

        # Navigate to Product A page
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Failed to click Product A link: {e}")

        # Add product to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click Add to cart button: {e}")

        # Click on the cart button
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button > img.icon[alt='cart']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click cart button: {e}")

        # Wait for the "GO TO CHECKOUT" button to be present
        try:
            go_to_checkout_button = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Failed to find or validate 'GO TO CHECKOUT' button: {e}")

if __name__ == "__main__":
    unittest.main()