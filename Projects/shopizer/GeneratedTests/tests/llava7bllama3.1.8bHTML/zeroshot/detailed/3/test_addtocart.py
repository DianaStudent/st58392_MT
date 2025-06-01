import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

class TestCartProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_cart_product(self):
        # Open the home page.
        self.driver.get('http://localhost:8000')

        # Click on a product item to reveal the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.product-name'))
        )
        add_to_cart_button.click()

        # Hover over the first product (assuming it's a link).
        product_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.product-link'))
        )
        self.driver.execute_script("arguments[0].hover();", product_link)

        # Click the revealed "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='add-to-cart']"))
        )
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon.
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.cart-icon'))
        )
        cart_icon.click()

        # Wait for the popup to become visible.
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'cart-popup'))
        )

        # Click "View cart" or similar button inside the popup.
        view_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='view-cart']"))
        )
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list.
        cart_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table.cart-list'))
        )
        self.assertTrue(cart_list.text.startswith('1 item'))

if __name__ == '__main__':
    unittest.main()