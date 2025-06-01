from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Accept cookies if present
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .icon-cart"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )

        # Check if the popup is visible
        if not cart_popup.is_displayed():
            self.fail("Cart popup did not become visible")

        # Click "View Cart" button inside the popup
        view_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
        )
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_item = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content tbody tr"))
        )

        if not cart_item:
            self.fail("No items found in the cart on the cart page.")

        product_name_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content tbody tr .product-name a"))
        )

        if not product_name_element:
            self.fail("Product name element not found in cart.")

        product_name = product_name_element.text
        if not product_name:
            self.fail("Product name is empty.")

        self.assertNotEqual(product_name, "", "Product name is empty")

if __name__ == "__main__":
    unittest.main()