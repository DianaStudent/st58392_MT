from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data["home_page"])

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver

        # 1. Open home page is already done in setUp

        # 2. Click on product category (e.g. Category A)
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()
        except:
            self.fail("Failed to find or click Category A link.")

        # Navigate to the page simulated for category A
        driver.get("data:text/html;charset=utf-8," + html_data["category_a_page"])

        # 3. Select the first product (e.g. Product A)
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except:
            self.fail("Failed to find or click Product A link.")

        # Navigate to the product page
        driver.get("data:text/html;charset=utf-8," + html_data["product_page"])

        # 4. Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Failed to find or click Add to Cart button.")
        
        # 5. Explicitly click the cart icon (shopping bag) to open the mini-cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except:
            self.fail("Failed to find or click the cart button.")

        # Move to "popup" page which simulates the opened mini-cart
        driver.get("data:text/html;charset=utf-8," + html_data["popup"])

        # 6. Wait for the mini-cart to become visible
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Go to checkout']"))
            )
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not visible in the mini-cart.")
        except:
            self.fail("Failed to find the GO TO CHECKOUT button in the mini-cart.")

if __name__ == "__main__":
    unittest.main()