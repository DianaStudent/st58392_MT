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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Category A
        try:
            category_a_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()
        except Exception as e:
            self.fail(f"Category A link not found: {e}")

        # Select Product A
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Product A link not found: {e}")

        # Click on Add to Cart button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {e}")

        # Click on cart button (shopping bag)
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found: {e}")

        # Wait for "GO TO CHECKOUT" button presence
        try:
            go_to_checkout_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Go to checkout')]"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to Checkout button is not visible")
        except Exception as e:
            self.fail(f"Go to checkout button not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()