from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.implicitly_wait(10)

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if prompt exists
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if accept_button.is_displayed():
                accept_button.click()
        except:
            pass  # If the button is not present or clickable, continue
        
        # Hover over the first product
        product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2:nth-of-type(1) .product-action-2 button[title='Add to cart']")
        ))
        
        # Hover to reveal the "Add to Cart" button
        ActionChains(driver).move_to_element(product).perform()

        # Click "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-wrap-2:nth-of-type(1) .product-action-2 button[title='Add to cart']")
        ))
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".header-right-wrap .icon-cart")
        ))
        cart_icon.click()

        # Wait for cart popup to be visible
        cart_popup = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content.active")
        ))

        # Ensure cart popup contains at least one item
        items_in_cart = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not items_in_cart:
            self.fail("No items present in the cart popup.")

        # Click "View Cart" button
        view_cart_button = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "View Cart")
        ))
        view_cart_button.click()

        # Verify product appears in the cart
        cart_page = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart-main-area")
        ))

        # Ensure the cart page contains the product
        products_in_cart = cart_page.find_elements(By.CSS_SELECTOR, ".product-name a")
        if not any("Olive Table" in product.text for product in products_in_cart):
            self.fail("Olive Table not found in cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()