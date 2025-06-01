from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Category A
        try:
            category_a = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
            category_a.click()
        except Exception as e:
            self.fail(f"Category A link not found: {str(e)}")

        # Click on Product A
        try:
            product_a = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
            product_a.click()
        except Exception as e:
            self.fail(f"Product A link not found: {str(e)}")

        # Add Product A to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {str(e)}")

        # Click on the cart button
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found: {str(e)}")

        # Check if "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mini-cart-open a.button.is-primary")))
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()