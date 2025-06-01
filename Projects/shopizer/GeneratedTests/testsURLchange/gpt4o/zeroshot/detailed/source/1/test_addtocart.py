import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            self.fail("Failed to locate or click on the accept cookies button")

        # Hover over the first product
        try:
            first_product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-img"))
            )
            ActionChains(driver).move_to_element(first_product).perform()
        except:
            self.fail("Failed to locate or hover over the first product")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Failed to locate or click on 'Add to cart' button")

        # Click the cart icon to open the popup cart
        try:
            cart_icon = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Failed to locate or click on the cart icon")

        # Wait for the popup to become visible
        try:
            wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
            )
        except:
            self.fail("Cart popup did not become visible")

        # Click "View Cart" in the popup
        try:
            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except:
            self.fail("Failed to locate or click on 'View Cart' button")

        # Verify that the product appears in the cart list
        try:
            cart_items = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart-table-content"))
            )
            self.assertTrue(cart_items.is_displayed(), "Cart items are not displayed.")
        except:
            self.fail("Failed to verify that cart items appear in the cart list")

if __name__ == "__main__":
    unittest.main()