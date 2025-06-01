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

        # Accept cookies if present
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
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
        shopping_cart_content_locator = (By.CLASS_NAME, "shopping-cart-content")
        wait.until(EC.presence_of_element_located(shopping_cart_content_locator))

        # Click "View Cart" button inside the popup
        view_cart_button_locator = (By.LINK_TEXT, "View Cart")
        view_cart_button = wait.until(EC.element_to_be_clickable(view_cart_button_locator))
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        product_name_locator = (By.XPATH, "//td[@class='product-name']/a")
        product_name_element = wait.until(EC.presence_of_element_located(product_name_locator))
        product_name = product_name_element.text

        if not product_name:
            self.fail("Product name not found in cart")

        self.assertIn("Olive Table", product_name, "Product not found in cart list")


if __name__ == "__main__":
    unittest.main()