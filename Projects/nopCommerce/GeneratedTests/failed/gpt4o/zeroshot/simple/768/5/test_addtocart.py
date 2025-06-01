from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Search for a book
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_box.send_keys("book")
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-box-button"))
        )
        search_button.click()

        # Wait for search results and add the first book to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Check for success notification
        success_notification = self.wait.until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )
        success_text = success_notification.text
        self.assertIn("The product has been added to your shopping cart", success_text, "Success notification not found.")

        # Check if cart contains at least one item
        cart_items = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flyout-cart .count a"))
        )
        cart_text = cart_items.text
        self.assertTrue(int(cart_text.split()[0]) >= 1, "Cart does not contain at least one item.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()