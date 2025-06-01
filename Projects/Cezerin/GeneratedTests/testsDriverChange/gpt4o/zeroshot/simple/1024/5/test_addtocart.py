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
    
    def test_add_to_cart(self):
        driver = self.driver
        
        # Navigate to Category A
        try:
            category_a_link = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a.has-items[href='/category-a']")
            ))
            category_a_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Category A: {str(e)}")
        
        # Navigate to Product A
        try:
            product_a_link = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='/category-a/product-a']")
            ))
            product_a_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Product A: {str(e)}")
        
        # Click Add to Cart button
        try:
            add_to_cart_button = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.button-addtocart button")
            ))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {str(e)}")
        
        # Click Cart button to view cart
        try:
            cart_button = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.cart-button img[title='cart']")
            ))
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to open cart: {str(e)}")

        # Verify presence of "GO TO CHECKOUT" button
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth[href='/checkout']")
            ))
        except TimeoutException:
            self.fail("GO TO CHECKOUT button is not present after adding product to cart.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()