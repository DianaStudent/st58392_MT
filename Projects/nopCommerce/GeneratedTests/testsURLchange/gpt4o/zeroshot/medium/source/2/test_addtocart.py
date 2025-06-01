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

        # Step 2: Click on the "Search" link in the top navigation
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link is missing")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_field:
            self.fail("Search field is missing")
        search_field.send_keys("book")

        search_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        if not search_button:
            self.fail("Search button is missing")
        search_button.click()

        # Step 4: On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button is missing")
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        success_notification = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        if not success_notification:
            self.fail("Success notification is missing")

        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Shopping cart link in notification is missing")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_items = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        if not cart_items:
            self.fail("Cart items are missing")

        cart_table = cart_items.find_element(By.CSS_SELECTOR, "table.cart")
        if not cart_table:
            self.fail("Cart table is missing")

        product_name = cart_table.find_element(By.CSS_SELECTOR, ".product-name").text
        if not product_name or product_name != "Book1":
            self.fail("The cart does not contain the expected product")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()