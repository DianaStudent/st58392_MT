from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on "Search" from the main menu
        search_menu = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        if not search_menu:
            self.fail("Search menu item is not found.")
        search_menu.click()
        
        # Type the search term "book" into the search field
        search_field = wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        if not search_field:
            self.fail("Search field is not found.")
        search_field.send_keys("book")
        
        # Submit the search
        search_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.search-box-button"))
        )
        if not search_button:
            self.fail("Search button is not found.")
        search_button.click()
        
        # Wait for the product grid to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid"))
        )
        
        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button is not found.")
        add_to_cart_button.click()
        
        # Wait for the notification bar to appear
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification"))
        )
        if not success_notification:
            self.fail("Success notification is not visible.")
        
        # Click the "shopping cart" link within the notification
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Cart link in notification is not found.")
        cart_link.click()
        
        # On the cart page, verify that the expected product is present
        cart_item_count = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product"))
        )
        if not cart_item_count:
            self.fail("Cart does not contain any items.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()