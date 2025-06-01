import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Navigate to the search page from the main menu
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        # Type the search term "book" into the search field
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.clear()
        search_input.send_keys("book")
        
        # Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        search_button.click()
        
        # Wait for the product grid to load and locate the first product's "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Wait for the notification bar to appear and verify it
        notification_bar = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.bar-notification.success")))
        
        self.assertIn("The product has been added to your", notification_bar.text)
        
        # Click on the "shopping cart" link in the notification
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()
        
        # Verify that the expected product is present in the cart
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.cart tbody tr")))
        self.assertGreaterEqual(len(cart_items), 1, "Cart does not contain any items")
        
        product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.product a.product-name")))
        self.assertEqual(product_name.text, "Book1", "Expected product is not present in the cart")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()