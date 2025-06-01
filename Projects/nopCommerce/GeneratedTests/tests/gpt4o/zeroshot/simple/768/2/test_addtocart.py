import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Locate the search box
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        if not search_box:
            self.fail("Search box not found")
        
        # Enter search text and submit
        search_box.send_keys("book")
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Wait for search results and click 'Add to cart' button for the first product
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Verify notification of item added to cart
        success_notification = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        if not success_notification:
            self.fail("Success notification not found")
        
        # Verify link to cart is present in the notification
        cart_link = success_notification.find_element(By.CSS_SELECTOR, "a[href='/cart']")
        if not cart_link:
            self.fail("Link to cart in success notification not found")

        # Verify cart contains at least one item
        cart_items_count = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".mini-shopping-cart .count"), "1 item(s)"))
        if not cart_items_count:
            self.fail("Cart does not contain any items")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()