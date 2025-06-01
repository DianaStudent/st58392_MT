```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.locator import Locator
from selenium.webdriver.support.wait import Wait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import get_driver

class TestScenario(unittest.TestCase):
    def setUp(self):
        driver = get_driver(ChromeDriverManager, 'https://example.com')
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_scenario(self):
        # Open the home page
        self.driver.get('http://localhost/')

        # Hover over the first product
        product_1_selector = Locator('html_data', 'class:product-item')
        product_1 = WebDriverWait(self.driver, 20).until(product_1_selector)

        # Click the revealed "Add to cart" button
        self.driver.execute_script('arguments[\'document.querySelector(\'.product-item\').querySelectorAll(".btn-cart")[0].click()\', arguments)')

        # Click the cart icon to open the popup cart
        cart_icon_selector = Locator('html_data', 'class:cart-icon')
        cart_icon = WebDriverWait(self.driver, 20).until(cart_icon_selector)
        self.driver.execute_script(f'arguments[\'document.querySelector(".btn-cart").parentElement.querySelector("{0}").click()\';, f'{cart_icon_selector}')

        # Wait for the popup to become visible
        popup_selector = Locator('html_data', 'class:popup')
        WebDriverWait(self.driver, 20).until(popup_selector)

        # Click "View cart" or similar button inside the popup
        view_cart_button_selector = Locator('html_data', 'class:view-cart')
        self.driver.execute_script(f'arguments[\'document.querySelector(".popup").querySelectorAll("{0}")[0].click()\';, f'{view_cart_button_selector}')

        # On the cart page, verify that the product appears in the cart list
        cart_list_selector = Locator('html_data', 'class:cart-list')
        cart_list = WebDriverWait(self.driver, 20).until(cart_list_selector)
        cart_item_selector = Locator('html_data', 'class:cart-item')
        self.assertTrue(product_1 in cart_list, f'Product {product_1} not found in cart list')

if __name__ == '__main__':
    unittest.main()
```