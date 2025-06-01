import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A page
        try:
            category_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except:
            self.fail("Could not find or click 'Category A' link.")

        # Navigate to Product A page
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except:
            self.fail("Could not find or click 'Product A' link.")

        # Add product to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click 'Add to cart' button.")

        # Click on the cart button
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button > img[alt='cart']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

        # Check for the presence of "GO TO CHECKOUT" button
        try:
            wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
        except:
            self.fail("Could not find 'GO TO CHECKOUT' button after adding to cart and opening cart.")


if __name__ == "__main__":
    unittest.main()