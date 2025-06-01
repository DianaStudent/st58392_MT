from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Wait for and accept cookies
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()

            # Hover over the first product to reveal the "Add to cart" button
            first_product = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(first_product).perform()

            # Click the revealed "Add to cart" button
            add_to_cart_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2 .fa-shopping-cart")))
            add_to_cart_button.click()

            # Click the cart icon to open the popup cart
            cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()

            # Wait for the cart popup to become visible
            cart_popup = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".shopping-cart-content.active")))

            # Verify the popup contains at least one item
            cart_count = int(wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".count-style"))).text)
            if cart_count < 1:
                self.fail("Cart popup does not contain any items.")

            # Click "View Cart" inside the popup
            view_cart_button = wait.until(EC.element_to_be_clickable(
                (By.LINK_TEXT, "VIEW CART")))
            view_cart_button.click()

            # Verify the product appears in the cart list
            cart_list = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".cart-main-area")))
            self.assertTrue(cart_list.is_displayed(), "Cart list is not displayed.")

        except Exception as e:
            # If any required element is missing, fail the test
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()