from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open home page
        self.driver.get("http://localhost:3000/")

        # Click on product category (e.g. Category A)
        category_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_link.click()

        # Select the first product (e.g. Product A)
        product_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/product-a']"))
        )
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button"))
        )
        add_to_cart_button.click()

        # Explicitly click the cart icon (shopping bag)
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_button.click()

        # Wait for the mini-cart to become visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mini-cart"))
        )

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "#mini-cart .button.is-success")
        self.assertIsNotNone(checkout_button.text)

if __name__ == "__main__":
    unittest.main()