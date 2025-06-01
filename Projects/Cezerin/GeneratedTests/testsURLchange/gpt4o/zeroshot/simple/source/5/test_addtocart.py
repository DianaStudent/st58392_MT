from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Category A
        try:
            category_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
            category_a.click()
        except Exception as e:
            self.fail(f"Category A link not found: {e}")

        # Select Product A
        try:
            product_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
            product_a.click()
        except Exception as e:
            self.fail(f"Product A link not found: {e}")
        
        # Click Add to Cart
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {e}")

        # Click on Cart
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'cart-button')]")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found: {e}")
        
        # Verify "GO TO CHECKOUT" presence
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT")))
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()