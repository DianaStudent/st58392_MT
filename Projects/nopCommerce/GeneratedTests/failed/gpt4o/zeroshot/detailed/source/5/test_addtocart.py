from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Home page
        driver.get("http://max/")
        
        # Click on "Search" from the main menu
        search_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_menu.click()
        
        # Type the search term "book" into the search field
        search_field = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_field.send_keys("book")
        
        # Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()
        
        # Wait for the product grid to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        
        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = product_grid.find_element(By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")
        add_to_cart_button.click()
        
        # Wait for the notification bar to appear
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        self.assertIn("The product has been added to your shopping cart", notification.text)
        
        # From the notification, click the "shopping cart" link
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()
        
        # On the cart page, verify that the expected product is present
        cart_page_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-name")))
        self.assertEqual(cart_page_product.text, "Book1")
        
        # Confirm cart contains at least one item
        cart_items = driver.find_elements(By.CSS_SELECTOR, ".product")
        self.assertGreaterEqual(len(cart_items), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()