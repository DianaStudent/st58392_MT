import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Category A
        try:
            category_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_a_link.click()
        except:
            self.fail("Category A link not found.")

        # Click on Product A
        try:
            product_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_a_link.click()
        except:
            self.fail("Product A link not found.")

        # Add Product A to the cart
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.button-addtocart button.button.is-success")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found.")

        # Click on the cart button
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button img[src='/assets/images/shopping-bag.svg']")))
            cart_button.click()
        except:
            self.fail("Cart button not found.")

        # Wait for "GO TO CHECKOUT" button to be present
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        except:
            self.fail("\"GO TO CHECKOUT\" button not found.")

if __name__ == "__main__":
    unittest.main()