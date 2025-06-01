import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Store
        try:
            store_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Medusa Store")))
            store_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to the store: {str(e)}")

        # Click first product (Medusa Sweatshirt)
        try:
            product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
            product_link.click()
        except Exception as e:
            self.fail(f"Failed to click on the product link: {str(e)}")

        # Select Size 'L'
        try:
            size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
            size_button.click()
        except Exception as e:
            self.fail(f"Failed to select size: {str(e)}")

        # Add to Cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {str(e)}")

        # Open Cart
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to open cart: {str(e)}")

        # Verify 'Go to checkout' button
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        except Exception as e:
            self.fail(f"'Go to checkout' button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()