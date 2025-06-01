import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Category A
        category_a_selector = "a[href='/category-a']"
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, category_a_selector))
        ).click()

        # Click on Product A
        product_a_selector = "a[href='/category-a/product-a']"
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, product_a_selector))
        ).click()

        # Add Product A to cart
        add_to_cart_button_selector = ".button-addtocart button"
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, add_to_cart_button_selector))
        ).click()

        # Click on cart button (shopping bag)
        cart_button_selector = ".cart-button"
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cart_button_selector))
        ).click()

        # Verify the presence of "GO TO CHECKOUT" button
        go_to_checkout_button_selector = ".button-primary"
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, go_to_checkout_button_selector))
            )
        except:
            self.fail("GO TO CHECKOUT button was not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()