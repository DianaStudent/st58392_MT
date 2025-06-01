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

        # Hover over the product image to reveal the "Add to cart" button
        product_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-img']"))
        )
        if product_element is None:
            self.fail("Product image not found")

        add_to_cart_button_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(add_to_cart_button_locator)
        )

        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button_locator)
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Open the cart popup by clicking the cart icon
        cart_icon_locator = (By.CLASS_NAME, "icon-cart")
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(cart_icon_locator)
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable")

        # Verify that at least one product is listed in the popup cart
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
            )
        except:
            self.fail("Cart popup not opened")

        cart_items_locator = (By.CLASS_NAME, "single-shopping-cart")
        try:
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(cart_items_locator)
            )
            if not cart_items:
                self.fail("No items found in the cart popup")
        except:
            self.fail("Could not find cart items")

        self.assertTrue(len(cart_items) > 0, "No items found in cart popup")

if __name__ == "__main__":
    unittest.main()