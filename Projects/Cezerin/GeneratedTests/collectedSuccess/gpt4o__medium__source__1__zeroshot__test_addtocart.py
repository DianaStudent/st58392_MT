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

        try:
            # Wait for the home page to load and click on the category for "Category A"
            category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            category_link.click()

            # Wait for the category page to load and click on the product link for "Product A"
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_link.click()

            # Wait for the product page to load and click on the 'Add to cart' button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()

            # Click on the cart button (shopping bag) to open the mini-cart
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
            )
            cart_button.click()

            # Check for the presence of the "GO TO CHECKOUT" button in the mini-cart
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
            
            # Check if the button exists and is not empty
            if not go_to_checkout_button.text.strip():
                self.fail("GO TO CHECKOUT button is present but is empty")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()