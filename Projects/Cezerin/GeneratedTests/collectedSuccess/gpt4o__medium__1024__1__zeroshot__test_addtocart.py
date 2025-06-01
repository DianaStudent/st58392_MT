import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the Category A link
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
        if not category_link:
            self.fail("Category link is missing.")
        category_link.click()

        # Select the first product (Product A)
        product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]')))
        if not product_link:
            self.fail("Product link is missing.")
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button')))
        if not add_to_cart_button:
            self.fail("Add to cart button is missing.")
        add_to_cart_button.click()

        # Click the shopping cart icon
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button')))
        if not cart_button:
            self.fail("Shopping cart button is missing.")
        cart_button.click()

        # Verify the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.button.is-primary.is-fullwidth')))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()