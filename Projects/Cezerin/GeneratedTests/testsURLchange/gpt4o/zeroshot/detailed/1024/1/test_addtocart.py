from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on "Category A" link
        category_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a_link.click()

        # Select "Product A"
        product_a_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart .button")))
        add_to_cart_button.click()

        # Explicitly click on the cart icon (shopping bag)
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Wait for mini-cart to be visible
        mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mini-cart-open")))

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = mini_cart.find_element(By.CSS_SELECTOR, ".button.is-primary.is-fullwidth")
        if not go_to_checkout_button or not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button is not present in mini-cart")

        # Check if the button has appropriate href attribute
        checkout_href = go_to_checkout_button.get_attribute("href")
        if not checkout_href or not checkout_href.endswith('/checkout'):
            self.fail("GO TO CHECKOUT button doesn't have correct href")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()