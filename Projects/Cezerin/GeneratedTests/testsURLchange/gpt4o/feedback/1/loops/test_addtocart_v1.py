import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/")
    
    def test_add_to_cart(self):
        driver = self.driver
        
        # Click on "Category A"
        category_a = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        category_a.click()

        # Select the first product
        first_product = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        first_product.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))
        )
        add_to_cart_button.click()

        # Click the cart icon/button
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'cart-button'))
        )
        cart_button.click()

        # Verify "GO TO CHECKOUT" button presence
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()