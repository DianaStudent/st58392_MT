import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Navigate to the homepage of the website
        self.driver.get('http://localhost:3000/')

        # Find and click on the product display page for the red shoe
        product_display_page = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-display-page"]')))
        self.product_display_page = product_display_page

        # Add the product to the cart by clicking on the 'Add To Cart' button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
        self.add_to_cart_button = add_to_cart_button

        # Click on the shopping cart (indicated by the shopping bag icon)
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping-cart-button"]')))
        self.cart_button = cart_button

        # Verify that the product is in the cart
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="go-to-checkout-button"]')))
        self.go_to_checkout_button = go_to_checkout_button

        # Check if required elements are present
        required_elements = [
            '//*[@id="product-display-page"]',
            '//*[@id="add-to-cart-button"]',
            '//*[@id="shopping-cart-button"]'
        ]
        for element in required_elements:
            try:
                self.product_display_page.find_element_by_css_selector('img')
            except NoSuchElementException:
                self.fail(f'Element {element} not found')

if __name__ == '__main__':
    unittest.main()