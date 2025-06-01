from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select as uiSelect
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_action import TouchAction

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver with ChromeDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tear down the webdriver
        self.driver.quit()

    def test_add_to_cart(self):
        try:
            # Open the home page of a store website
            self.driver.get("http://localhost:3000/")

            # Click on the first product category (Category A)
            category_button = self.wait_and_click(".nav-link-item", "data-toggle='category' data-category='Category A'")

            # Select the first product (Product A) from the cart
            product_button = self.wait_and_click(".btn[data-product='Product A']", 'class="product-name')

            # Click the shopping cart icon to open the mini-cart
            cart_button = self.wait_and_click(".cart-button", 'class="mini-cart')

            # Wait for the mini-cart to become visible
            WebDriverWait(self.driver, 20).until(lambda x: "div" in x.page_source and "GO TO CHECKOUT" in x.page_source)

            # Verify that the GO TO CHECKOUT button is present inside the cart
            checkout_button = self.wait_and_click(".btn[role='button'][data-cart-item][data-product='Product A']", 'class="mini-cart')

        except Exception as e:
            # If any required element is missing, fail the test
            self.fail(str(e))

    def wait_and_click(self, selector, condition):
        # Wait for 20 seconds before interacting with elements
        try:
            WebDriverWait(self.driver, 20).until(condition)

            # Click on the selected element using ActionChains
            action = ActionChains()
            return action.click_element(element=selector)
        except Exception as e:
            # Raise an error if the condition is not met within 20 seconds
            raise e

if __name__ == '__main__':
    unittest.main()