import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable.")

        # Find the first product and hover over it
        try:
            first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(first_product).perform()
        except:
            self.fail("First product not found or unable to hover.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable.")

        # Click the cart icon to open cart popup
        try:
            cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable.")

        # Wait for the popup to become visible
        try:
            shopping_cart_content = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
            )
        except:
            self.fail("Shopping cart popup is not visible.")

        # Verify cart contains at least one item
        try:
            items_in_cart = shopping_cart_content.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            if len(items_in_cart) == 0:
                self.fail("No items found in the cart.")
        except:
            self.fail("Unable to locate items in the cart popup.")

        # Click "View Cart" inside the popup
        try:
            view_cart_button = shopping_cart_content.find_element(By.LINK_TEXT, "View Cart")
            view_cart_button.click()
        except:
            self.fail("View Cart button not found or not clickable.")

        # Verify that the product appears in the cart list on the cart page
        try:
            cart_table_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content")))
            cart_items = cart_table_content.find_elements(By.CSS_SELECTOR, "tbody tr")
            if len(cart_items) == 0:
                self.fail("No items found in the cart page.")
        except:
            self.fail("Cart table content not found or empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()