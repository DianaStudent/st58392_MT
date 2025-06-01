import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://localhost:8000/dk')

    def test_add_to_cart(self):
        # Add a product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']")))
        add_to_cart_button.click()

        # Click on the cart button (shopping bag)
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-test='cart-icon']")))
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()