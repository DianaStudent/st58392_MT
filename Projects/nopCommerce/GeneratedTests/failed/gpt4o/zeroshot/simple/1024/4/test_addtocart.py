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
        self.driver.get("http://max/")
    
    def test_add_to_cart(self):
        driver = self.driver

        # Search for a book
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_box.send_keys("book")

        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Add the first book to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Check success notification
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )
        
        success_message = success_notification.text

        if "The product has been added to your" not in success_message:
            self.fail("Success notification not displayed or incorrect.")
        
        cart_link = success_notification.find_element(By.TAG_NAME, "a")
        if cart_link is None:
            self.fail("Cart link not found in success notification.")
        
        cart_link.click()
        
        # Verify cart has at least one item
        cart_count = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-shopping-cart .count"))
        )
        if "1 item(s)" not in cart_count.text:
            self.fail("Cart does not contain at least one item.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()