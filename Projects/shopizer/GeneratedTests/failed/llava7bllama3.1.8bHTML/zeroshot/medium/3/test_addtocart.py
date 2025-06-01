from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestCart(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_cart(self):
        # 1. Open the home page.
        self.assertEqual(self.driver.title, "Default store")

        # 2. Hover over a product image to reveal the "Add to cart" button.
        product_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@src='http://localhost:8080/static/files/DEFAULT/PRODUCTS/product1.jpg']")))
        product_image.location_once_scrolled_into_view
        self.assertEqual(product_image.get_attribute('alt'), 'Product 1')

        # 3. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#']//button[@class='add-to-cart-btn']")))
        self.assertEqual(add_to_cart_button.text, 'Add to Cart')
        add_to_cart_button.click()

        # 4. Open the cart popup by clicking the cart icon.
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-icon']")))
        self.assertEqual(cart_icon.text, 'Cart (1)')
        cart_icon.click()

        # 5. Verify that at least one product is listed in the popup cart.
        cart_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-popup']")))
        self.assertEqual(cart_popup.text, 'Your Cart')

        # Confirm success by checking that the popup contains at least one item.
        product_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-popup']//h5[1]"))).text
        self.failUnless(product_name.startswith('Product 1'))

if __name__ == '__main__':
    unittest.main()