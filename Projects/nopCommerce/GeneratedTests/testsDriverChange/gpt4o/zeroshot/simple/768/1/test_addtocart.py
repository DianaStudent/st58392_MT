import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTestCase(unittest.TestCase):
    
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        
        # Search for a book using the search box
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box not found")
        
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the search results to load and add the first book to the cart
        try:
            add_to_cart_buttons = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart buttons not found in search results")
        
        add_to_cart_buttons[0].click()
        
        # Verify the success notification is visible and contains a link to the cart
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success a[href='/cart']"))
            )
        except:
            self.fail("Success notification or link to cart not found")
        
        # Confirm the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".flyout-cart .count"), "1 item(s)")
            )
            self.assertTrue(cart_count)
        except:
            self.fail("Cart does not contain the expected number of items")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()