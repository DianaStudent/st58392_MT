import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://example.com")  # Replace with the actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        # Navigate to the homepage
        self.driver.get("http://example.com")  # Replace with the actual URL
        
        # Click on "Search" from the main menu
        search_menu_item = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_menu_item:
            self.fail("Search menu item is not found")
        search_menu_item.click()

        # Type the search term "book" into the search field
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        if not search_input:
            self.fail("Search input field is not found")
        search_input.send_keys("book")

        # Submit the search
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        if not search_button:
            self.fail("Search button is not found or not clickable")
        search_button.click()

        # Wait for the product grid to load
        product_grid = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid")))
        if not product_grid:
            self.fail("Product grid did not load")

        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button is not found")
        add_to_cart_button.click()

        # Wait for the notification bar to appear
        success_notification = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )
        if not success_notification or not success_notification.is_displayed():
            self.fail("Success notification did not appear")

        # Verify the notification contains a link to the cart
        cart_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        if not cart_link:
            self.fail("Cart link in notification is not found")
        cart_link.click()

        # On the cart page, verify that the expected product is present
        cart_items_count = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mini-shopping-cart .count a")))
        if not cart_items_count:
            self.fail("Cart items count element is not found")
        cart_items_text = cart_items_count.text
        if not cart_items_text or '1 item(s)' not in cart_items_text:
            self.fail("Expected product is not present in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()