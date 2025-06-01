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
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Category A
        try:
            category_a = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a.click()
        except Exception as e:
            self.fail("Category A link not found")

        # Select Product A
        try:
            product_a = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a.click()
        except Exception as e:
            self.fail("Product A link not found")

        # Add Product A to Cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-addtocart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button not found")

        # Click on Cart Button (shopping bag)
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except Exception as e:
            self.fail("Cart button not found")

        # Verify "GO TO CHECKOUT" button presence
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT"))
            )
        except Exception as e:
            self.fail("GO TO CHECKOUT button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()