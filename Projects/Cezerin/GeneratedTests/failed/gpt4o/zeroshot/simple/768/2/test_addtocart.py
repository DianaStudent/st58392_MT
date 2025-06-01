from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Navigate to Category A page
        try:
            category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
            category_a_link.click()
        except Exception as e:
            self.fail(f"Category A link not found: {str(e)}")
        
        # Click on Product A
        try:
            product_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
            product_a_link.click()
        except Exception as e:
            self.fail(f"Product A link not found: {str(e)}")
        
        # Add Product A to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to Cart button not found: {str(e)}")

        # Click on the cart button
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img[title='cart']")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found: {str(e)}")

        # Check for "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
        except Exception as e:
            self.fail(f"'GO TO CHECKOUT' button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()