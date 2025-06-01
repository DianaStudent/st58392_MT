import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept Cookies
        try:
            cookie_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            self.assertIsNotNone(cookie_button, "Cookie accept button not found.")
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie button acceptance failed: {str(e)}")

        # Wait for the product area
        try:
            product_area = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-area"))
            )
            self.assertIsNotNone(product_area, "Product area not found.")
        except Exception as e:
            self.fail(f"Product area not found: {str(e)}")

        # Hover over the first product to reveal the "Add to cart" button
        try:
            first_product = product_area.find_elements(By.CLASS_NAME, "product-wrap-2")[0]
            self.assertIsNotNone(first_product, "First product not found.")

            action = ActionChains(driver)
            action.move_to_element(first_product).perform()
        except Exception as e:
            self.fail(f"Hover over first product failed: {str(e)}")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = first_product.find_element(
                By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"
            )
            self.assertIsNotNone(add_to_cart_button, "Add to cart button not found.")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Clicking 'Add to cart' failed: {str(e)}")

        # Click the cart icon to open the popup cart
        try:
            cart_icon = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            self.assertIsNotNone(cart_icon, "Cart icon not found.")
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon click failed: {str(e)}")

        # Wait for the cart popup to become visible
        try:
            cart_popup = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
            )
            self.assertTrue(cart_popup.is_displayed(), "Cart popup not visible.")
        except Exception as e:
            self.fail(f"Cart popup visibility failed: {str(e)}")

        # Confirm the popup contains at least one item
        try:
            cart_items = cart_popup.find_elements(By.CLASS_NAME, "single-shopping-cart")
            self.assertGreater(len(cart_items), 0, "No items in cart popup.")
        except Exception as e:
            self.fail(f"Cart items retrieval failed: {str(e)}")

        # Click "View Cart" inside the popup
        try:
            view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
            self.assertIsNotNone(view_cart_button, "View Cart button not found in popup.")
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Clicking 'View Cart' failed: {str(e)}")

        # On the cart page, verify the product appears in the cart list
        try:
            cart_main_area = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart-main-area"))
            )
            self.assertIsNotNone(cart_main_area, "Cart main area not found.")

            cart_table = driver.find_element(By.CLASS_NAME, "cart-table-content")
            self.assertIsNotNone(cart_table, "Cart table not found.")

            cart_table_rows = cart_table.find_elements(By.TAG_NAME, "tr")
            self.assertGreater(len(cart_table_rows), 1, "No items listed in cart.")
        except Exception as e:
            self.fail(f"Verification on cart page failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()