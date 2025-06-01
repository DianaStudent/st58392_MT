import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except TimeoutException:
            self.fail("Timeout waiting for cookies button.")

        # Locate the first product and hover over it
        try:
            product_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            ActionChains(driver).move_to_element(product_element).perform()
        except TimeoutException:
            self.fail("Timeout locating the first product to hover over.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = product_element.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            self.wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()
        except TimeoutException:
            self.fail("Timeout waiting for 'Add to cart' button.")

        # Ensure the cart count has updated
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".icon-cart .count-style"), "1")
            )
        except TimeoutException:
            self.fail("Cart count did not update to 1.")

        # Click the cart icon to open the popup
        try:
            cart_icon_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_icon_button.click()
        except TimeoutException:
            self.fail("Timeout locating the cart icon for clicking.")

        # Wait for the popup to become visible
        try:
            cart_popup = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content"))
            )
        except TimeoutException:
            self.fail("Cart popup did not become visible.")

        # Ensure the popup is not empty
        cart_items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not cart_items:
            self.fail("Cart popup is empty, expected at least one item.")
        
        # Click "View Cart" in the popup
        try:
            view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
            self.wait.until(EC.element_to_be_clickable(view_cart_button)).click()
        except TimeoutException:
            self.fail("Timeout waiting for 'View Cart' button in popup.")

        # Verify the product appears in the cart list
        try:
            cart_page = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area"))
            )
            cart_items_list = cart_page.find_elements(By.CSS_SELECTOR, ".cart-table-content tbody tr")
            if not cart_items_list:
                self.fail("No items found in the cart list on the cart page.")
        except TimeoutException:
            self.fail("Timeout waiting for cart page to load.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()