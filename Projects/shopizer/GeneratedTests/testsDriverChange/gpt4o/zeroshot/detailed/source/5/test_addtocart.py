import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        # Accept cookies
        accept_cookies_btn = self.wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button')))
        accept_cookies_btn.click()

        # Hover over the first product
        first_product = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2 .product-action-2 button[title='Add to cart']")
        ))
        ActionChains(self.driver).move_to_element(first_product).perform()

        # Click "Add to cart" button
        add_to_cart_btn = self.driver.find_element(
            By.CSS_SELECTOR, ".product-wrap-2 .product-action-2 button[title='Add to cart']")
        add_to_cart_btn.click()

        # Click the cart icon to open the popup cart
        cart_icon = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".header-right-wrap .icon-cart"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )

        # Click "View Cart"
        view_cart_btn = self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "View Cart"))
        )
        view_cart_btn.click()

        # On the cart page, verify that the product appears in the cart list
        cart_items = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart-table-content tbody tr"))
        )
        self.assertTrue(cart_items, "No items found in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()