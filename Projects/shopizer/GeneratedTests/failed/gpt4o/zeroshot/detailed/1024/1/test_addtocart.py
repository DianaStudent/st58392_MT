from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the button is present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_locator = (By.CSS_SELECTOR, "div.product-wrap-2:nth-child(1)")
        product_element = wait.until(EC.presence_of_element_located(product_locator))
        self.assertTrue(product_element.is_displayed(), "Product element not visible.")
        
        action = ActionChains(driver)
        action.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        add_to_cart_button_locator = (By.CSS_SELECTOR, "div.product-wrap-2:nth-child(1) button[title='Add to cart']")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_button_locator))
        add_to_cart_button.click()

        # Click the cart icon to open the cart popup
        cart_icon_locator = (By.CSS_SELECTOR, "button.icon-cart")
        cart_icon = wait.until(EC.element_to_be_clickable(cart_icon_locator))
        cart_icon.click()

        # Wait for the cart popup to become visible
        cart_popup_locator = (By.CSS_SELECTOR, "div.shopping-cart-content.active")
        cart_popup = wait.until(EC.visibility_of_element_located(cart_popup_locator))
        self.assertTrue(cart_popup.is_displayed(), "Cart popup not visible.")

        # Click "View Cart" inside the popup
        view_cart_button_locator = (By.CSS_SELECTOR, "a.default-btn[href='/cart']")
        view_cart_button = wait.until(EC.element_to_be_clickable(view_cart_button_locator))
        view_cart_button.click()

        # Verify that the product appears in the cart list on the cart page
        cart_list_locator = (By.CSS_SELECTOR, "div.cart-main-area")
        cart_list = wait.until(EC.presence_of_element_located(cart_list_locator))
        self.assertTrue(cart_list.is_displayed(), "Cart list not visible.")

        product_name_locator = (By.CSS_SELECTOR, "td.product-name a")
        product_name = wait.until(EC.presence_of_element_located(product_name_locator))
        self.assertTrue(product_name.is_displayed(), "Product name not displayed in cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()