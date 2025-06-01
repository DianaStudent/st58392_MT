from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Click on the "Search" link in the top navigation
        search_menu_selector = "a[href='/search']"
        search_menu = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, search_menu_selector)))
        search_menu.click()
        
        # Step 3: Enter "book" in the search field and submit the search
        search_field_selector = "#q"
        search_button_selector = "button.button-1.search-button"
        
        search_field = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_field_selector)))
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_button_selector)))
        
        if not search_field or not search_button:
            self.fail("Search field or search button not found.")
        
        search_field.clear()
        search_field.send_keys("book")
        search_button.click()
        
        # Step 4: On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button_selector = "button.button-2.product-box-add-to-cart-button"
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, add_to_cart_button_selector)))
        
        if not add_to_cart_button:
            self.fail("Add to Cart button not found.")
        
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        bar_notification_selector = "#bar-notification"
        bar_notification = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, bar_notification_selector)))

        if not bar_notification or "The product has been added to your shopping cart" not in bar_notification.text:
            self.fail("Success notification not found or incorrect.")
        
        # Step 6: Click the "shopping cart" link inside the notification
        cart_link_selector = "#bar-notification a"
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cart_link_selector)))
        cart_link.click()
        
        # Step 7: Confirm success by checking that the cart page contains the added product
        cart_items_selector = "table.cart tbody tr"
        cart_items = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cart_items_selector)))

        if not cart_items or len(cart_items) == 0:
            self.fail("Cart does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()