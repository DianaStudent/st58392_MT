from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Navigate to the homepage
        driver.get("http://max/")

        # Step 2: Click on "Search" from the main menu
        try:
            search_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
            search_menu.click()
        except Exception as e:
            self.fail(f"Search menu not found or not clickable: {str(e)}")

        # Step 3: Type "book" in the search field
        try:
            search_field = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_field.clear()
            search_field.send_keys("book")
        except Exception as e:
            self.fail(f"Search field not found or not interactable: {str(e)}")

        # Step 4: Submit the search
        try:
            search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-box-button")))
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found or not interactable: {str(e)}")

        # Step 5: Wait for the product grid to load
        try:
            product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        except Exception as e:
            self.fail(f"Product grid not loaded: {str(e)}")

        # Step 6: Locate and click the "Add to cart" button for the first product
        try:
            first_product_add_to_cart = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
            first_product_add_to_cart.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickbale: {str(e)}")

        # Step 7: Wait for success notification
        try:
            notification = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".bar-notification.success .content")
                )
            )
            self.assertIn("The product has been added to your shopping cart", notification.text)
        except Exception as e:
            self.fail(f"Success notification not visible or incorrect: {str(e)}")

        # Step 8: Click the "shopping cart" link in the notification
        try:
            cart_link = notification.find_element(By.TAG_NAME, "a")
            cart_link.click()
        except Exception as e:
            self.fail(f"Shopping cart link not found in notification: {str(e)}")

        # Step 9: Verify that the expected product is present in the cart
        try:
            cart_items = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-page tbody"))
            )
            items = cart_items.find_elements(By.CSS_SELECTOR, "tr")
            self.assertTrue(len(items) > 0, "Cart is empty, but expected item(s) present.")
        except Exception as e:
            self.fail(f"Shopping cart verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()