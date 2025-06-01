import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.get("https://example.com")

        # Step 2: Click on product category
        select_category = WebDriverWait(self.driver, 20).until(EC.element_located_by_css_selector('select[name="category"]'))
        select_category.select_by_value("Category A")
        self.assertEqual(select_category.all_selected_options[0].text, "Category A")

        # Step 3: Select the first product
        select_product = WebDriverWait(self.driver, 20).until(EC.element_located_by_css_selector('select[name="product"]'))
        select_product.select_by_index(0)
        self.assertEqual(select_product.all_selected_options[0].text, "Product A")

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_located_by_css_selector('button[name="add-to-cart"]'))
        add_to_cart_button.click()

        # Step 5: Open the shopping bag
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_located_by_css_selector('div[role="region"][class="cart-button"]'))
        cart_icon.click()
        cart_popup = WebDriverWait(self.driver, 20).until(EC.element_located_by_css_selector('div[role="dialog"][aria-labelledby="shopping-cart-popover-1"]'))

        # Step 6: Verify the "GO TO CHECKOUT" button is present
        go_to_checkout_button = WebDriverWait(cart_popup, 20).until(EC.element_located_by_css_selector('button[title="Go to Checkout"]'))
        self.assertIsNotNone(go_to_checkout_button)

if __name__ == '__main__':
    unittest.main()