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
    
    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open home page
        try:
            driver.get("http://localhost:3000/")
        except Exception as e:
            self.fail("Failed to open home page: " + str(e))
        
        # Step 2: Click on product category
        try:
            category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_link.click()
        except Exception as e:
            self.fail("Failed to find or click on product category: " + str(e))
        
        # Step 3: Select the first product
        try:
            product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_link.click()
        except Exception as e:
            self.fail("Failed to find or click on the first product: " + str(e))
        
        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Failed to find or click on 'Add to cart' button: " + str(e))

        # Step 5: Click the cart icon/button to open the shopping bag
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
            cart_button.click()
        except Exception as e:
            self.fail("Failed to find or click on cart icon/button: " + str(e))

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
            self.assertIsNotNone(go_to_checkout_button.text.strip(), "GO TO CHECKOUT button is present but empty")
        except Exception as e:
            self.fail("Failed to find 'GO TO CHECKOUT' button: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()