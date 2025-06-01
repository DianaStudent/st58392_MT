from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(first_product_locator)
            )
        except:
            self.fail("First product not found")

        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button_locator = (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button_locator)
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CSS_SELECTOR, ".icon-cart i.pe-7s-shopbag")
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(cart_icon_locator)
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable")

        # Wait for the popup to become visible
        cart_popup_locator = (By.CSS_SELECTOR, ".shopping-cart-content.active")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(cart_popup_locator)
            )
        except:
            self.fail("Cart popup did not appear")

        # Click "View cart" button inside the popup
        view_cart_button_locator = (By.LINK_TEXT, "View Cart")
        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(view_cart_button_locator)
            )
            view_cart_button.click()
        except:
            self.fail("View Cart button not found or not clickable")

        # On the cart page, verify that the product appears in the cart list
        cart_item_locator = (By.CSS_SELECTOR, ".cart-main-area .cart-table-content tbody tr")
        try:
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(cart_item_locator)
            )
            if not cart_items:
                self.fail("No items found in the cart")
        except:
            self.fail("Could not locate cart items")

        self.assertTrue(len(cart_items) > 0, "No product found in the cart list.")

if __name__ == "__main__":
    unittest.main()