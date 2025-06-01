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
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the consent form is present
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")
        first_product = wait.until(EC.presence_of_element_located(first_product_locator))
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_button_locator))
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CLASS_NAME, "icon-cart")
        cart_icon = wait.until(EC.element_to_be_clickable(cart_icon_locator))
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup_locator = (By.CLASS_NAME, "shopping-cart-content.active")
        wait.until(EC.presence_of_element_located(cart_popup_locator))

        # Click "View cart" button inside the popup
        view_cart_button_locator = (By.LINK_TEXT, "View Cart")
        view_cart_button = wait.until(EC.element_to_be_clickable(view_cart_button_locator))
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_item_locator = (By.CLASS_NAME, "cart-table-content")
        cart_item = wait.until(EC.presence_of_element_located(cart_item_locator))

        if cart_item and cart_item.text:
            self.assertTrue(len(cart_item.find_elements(By.TAG_NAME, "tr")) > 1, "Cart is empty")
        else:
            self.fail("Cart item not found or empty.")

if __name__ == "__main__":
    unittest.main()