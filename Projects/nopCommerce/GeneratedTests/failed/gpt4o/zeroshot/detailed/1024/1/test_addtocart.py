from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Navigate to the homepage (already done in setUp)
        
        # Step 2: Click on "Search" from the main menu
        search_menu = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".top-menu.notmobile a[href='/search']")))
        search_menu.click()
        
        # Step 3: Type the search term "book" into the search field
        search_input = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#q")))
        search_input.clear()
        search_input.send_keys("book")
        
        # Step 4: Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_button.click()
        
        # Step 5: Wait for the product grid to load
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".products-wrapper .item-grid .item-box")))
        
        # Step 6: Locate the first product result and click the "Add to cart" button
        add_to_cart_button = driver.find_element(
            By.CSS_SELECTOR, ".product-box-add-to-cart-button")
        add_to_cart_button.click()
        
        # Step 7: Wait for the notification bar to appear
        notification_bar = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".bar-notification.success")))
        
        # Ensure the notification contains the correct text and a link to the cart
        notification_text = driver.find_element(By.CSS_SELECTOR, ".bar-notification.success p.content").text
        self.assertIn("The product has been added to your shopping cart", notification_text)
        
        cart_link = driver.find_element(By.CSS_SELECTOR, ".bar-notification.success p.content a[href='/cart']")
        cart_link.click()
        
        # Step 9: On the cart page, verify that the expected product is present
        cart_item_count = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".count a[href='/cart']")))
        cart_text = cart_item_count.text
        self.assertTrue("1 item(s)" in cart_text, "The cart does not contain the expected number of items.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()