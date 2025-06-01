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
        add_to_cart_button_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button_locator)
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CLASS_NAME, "icon-cart")
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(cart_icon_locator)
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable")

        # Wait for the popup to become visible
        shopping_cart_content_locator = (By.CLASS_NAME, "shopping-cart-content.active")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(shopping_cart_content_locator)
            )
        except:
            self.fail("Shopping cart content not found")

        # Click "View cart" button inside the popup
        view_cart_button_locator = (By.XPATH, "//div[@class='shopping-cart-content active']//a[text()='View Cart']")
        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(view_cart_button_locator)
            )
            view_cart_button.click()
        except:
            self.fail("View Cart button not found or not clickable")

        # On the cart page, verify that the product appears in the cart list
        product_name_locator = (By.XPATH, "//td[@class='product-name']/a")
        try:
            product_name_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(product_name_locator)
            )
            product_name = product_name_element.text
            self.assertTrue(product_name != "")
        except:
            self.fail("Product name not found on cart page or is empty")

if __name__ == "__main__":
    unittest.main()