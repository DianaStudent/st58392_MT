from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open home page
        home_page_url = 'http://localhost:3000/' + html_data["home_page"]
        driver.get(home_page_url)
        
        # Step 2: Click on product category
        category_a_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_a_link.click()
        
        # Step 3: Select the first product
        first_product_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        first_product_link.click()
        
        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )
        add_to_cart_button.click()
        
        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']"))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "Checkout button not found in the cart")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()