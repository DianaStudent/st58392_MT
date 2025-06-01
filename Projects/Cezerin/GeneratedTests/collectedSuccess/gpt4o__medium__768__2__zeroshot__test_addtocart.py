from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page and click on product category.
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 2: Select the first product.
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        first_product.click()

        # Step 3: Click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Step 5: Verify that the "GO TO CHECKOUT" button is present inside the cart.
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        
        if not checkout_button:
            self.fail("GO TO CHECKOUT button is not present inside the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()