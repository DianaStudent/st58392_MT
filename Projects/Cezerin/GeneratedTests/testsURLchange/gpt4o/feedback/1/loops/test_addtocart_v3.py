import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Category A" link
        category_a_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]')))
        category_a_link.click()

        # Click on the first product
        first_product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]')))
        first_product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button')))
        add_to_cart_button.click()

        # Click the cart icon/button
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button')))
        cart_button.click()

        # Verify "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed.")
        except Exception as e:
            self.fail(f"Failed to find 'GO TO CHECKOUT' button: {str(e)}")

if __name__ == "__main__":
    unittest.main()