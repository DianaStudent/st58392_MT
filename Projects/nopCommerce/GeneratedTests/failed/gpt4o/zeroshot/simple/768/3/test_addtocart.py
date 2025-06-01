from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)  # Wait for up to 20 seconds

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Search for a book
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        search_button.click()
        
        # Step 2: Click 'Add to cart' for the first book in search results
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Step 3: Wait for success notification
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        
        # Step 4: Verify success notification is visible and contains a link to the cart
        notification_text = notification.text
        self.assertIn("The product has been added to your shopping cart", notification_text, "Success notification text is incorrect.")
        self.assertIn("/cart", notification.text, "Success notification does not contain a link to the cart.")
        
        # Step 5: Confirm cart contains at least one item
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flyout-cart div.count a[href='/cart']")))
        cart_item_count = cart_link.text
        self.assertIn("1 item(s)", cart_item_count, "The cart does not contain the expected number of items.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()