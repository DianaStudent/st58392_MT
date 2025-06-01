from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Step 2: Click on product category
        category_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_link.click()

        # Step 3: Select the first product
        product_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        product_link.click()
        
        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
        )

        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not present in the cart.")
        
    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()