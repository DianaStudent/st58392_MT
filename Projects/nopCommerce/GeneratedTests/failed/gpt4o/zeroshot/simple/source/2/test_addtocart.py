from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Search for a book
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search input not found.")
        
        search_box.send_keys("book")
        
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        except:
            self.fail("Search button not found.")
        
        search_button.click()

        # Add the first book to the cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found.")
        
        add_to_cart_button.click()

        # Check for success notification
        try:
            success_notification = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
            )
        except:
            self.fail("Success notification not found.")
        
        self.assertIn("/cart", success_notification.find_element(By.TAG_NAME, "a").get_attribute("href"))

        # Confirm there is at least one item in the cart
        try:
            cart_item_count = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-shopping-cart .count a"))
            )
        except:
            self.fail("Cart item count not found.")
        
        self.assertIn("item(s)", cart_item_count.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()