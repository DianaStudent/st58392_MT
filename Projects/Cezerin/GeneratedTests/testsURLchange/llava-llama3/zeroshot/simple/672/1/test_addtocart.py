import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.actions import ActionAlert
from selenium.webdriver.support.ui import Alert
from selenium.webdriver.support.ui import Alerts

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome('chromedriver')
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        # Navigate to the website
        self.driver.get("http://localhost:3000/")

        # Add a product to cart
        product_name = Select(self.driver.find_element_by_id('product-name'))
        product_name.select_by_visible_text("Fresh Foam Cruz")
        product_price = self.driver.find_element_by_id('product-price')
        product_quantity = self.driver.find_element_by_id('product-quantity')

        product_price.send_keys("49.00")
        product_quantity.send_keys("1")

        # Click on the cart button
        cart_button = self.driver.find_element_by_id('cart-button')
        cart_button.click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'go-to-checkout'))
            )
        except:
            return False

        # Check for the presence of 'GO TO CHECKOUT' button
        self.assertTrue('GO TO CHECKOUT' in self.driver.title)

if __name__ == '__main__':
    unittest.main()