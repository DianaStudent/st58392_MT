import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')

    def test_add_to_cart(self):
        # Open home page
        driver = self.driver

        # Click on product category
        category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))
        )
        category_link.click()

        # Select the first product
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/1']"))
        )
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart']"))
        )
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag.
        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_icon.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-test='go-to-checkout']"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()