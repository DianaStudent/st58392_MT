import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080')  # Use the actual URL of the home page
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        # Home page is already opened in setUp()

        # Step 2: Hover over a product image to reveal the "Add to cart" button
        product_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
        self.assertIsNotNone(product_element, "Product image not found.")
        
        # Use ActionChains to hover over the product
        ActionChains(driver).move_to_element(product_element).perform()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        self.assertIsNotNone(add_to_cart_button, "Add to cart button not found.")
        
        add_to_cart_button.click()

        # Step 4: Open the cart popup by clicking the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        self.assertIsNotNone(cart_icon, "Cart icon not found.")
        
        cart_icon.click()

        # Step 5: Verify that at least one product is listed in the popup cart
        popup_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content")))
        self.assertIsNotNone(popup_cart, "Cart popup did not open.")
        
        products_in_cart = driver.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not products_in_cart:
            self.fail("No products found in the cart popup.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()