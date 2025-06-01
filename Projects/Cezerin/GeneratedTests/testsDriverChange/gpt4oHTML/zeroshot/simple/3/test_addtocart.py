import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        # Use webdriver-manager to manage ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/") # Replace with the correct URL
    
    def test_add_to_cart(self):
        driver = self.driver

        # Wait until the page is fully loaded and check the presence of homepage elements
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "home-slider"))
            )
        except Exception:
            self.fail("Home page did not load properly.")

        # Navigate to Category A page
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.has-items[href='/category-a']"))
            )
            category_a_link.click()
        except Exception:
            self.fail("Failed to locate and click on Category A link.")

        # Wait until the Category A page is loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-category"))
            )
        except Exception:
            self.fail("Category A page did not load properly.")

        # Click on Product A
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_a_link.click()
        except Exception:
            self.fail("Failed to locate and click on Product A link.")

        # Ensure Product Page is loaded by checking product-specific elements
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-product"))
            )
        except Exception:
            self.fail("Product page did not load properly.")

        # Click "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button-addtocart > button"))
            )
            add_to_cart_button.click()
        except Exception:
            self.fail("Failed to locate or click the 'Add to cart' button.")

        # Click on the cart button (shopping bag)
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button"))
            )
            cart_button.click()
        except Exception:
            self.fail("Failed to locate or click the cart button.")

        # Wait for presence of "GO TO CHECKOUT" button as confirmation of successful add to cart
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
        except Exception:
            self.fail("GO TO CHECKOUT button not present, indicating an unsuccessful add to cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()