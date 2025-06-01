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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Navigate to Search
        try:
            search_menu = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_menu.click()
        except Exception as e:
            self.fail(f"Search menu link not found or not clickable: {str(e)}")

        # Enter search term
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_box.send_keys("book")
        except Exception as e:
            self.fail(f"Search input box not found or not interactable: {str(e)}")
        
        # Submit search
        try:
            search_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-1.search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found or not clickable: {str(e)}")

        # Wait for product grid to load and find first product
        try:
            product = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-item"))
            )
            add_to_cart_button = product.find_element(By.CSS_SELECTOR, "button.product-box-add-to-cart-button")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {str(e)}")

        # Wait for success notification
        try:
            notification = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
            )
            content = notification.find_element(By.CLASS_NAME, "content")
            cart_link = content.find_element(By.LINK_TEXT, "shopping cart")
            cart_link.click()
        except Exception as e:
            self.fail(f"Success notification or shopping cart link not found: {str(e)}")

        # Verify the cart
        try:
            cart_items = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart"))
            )
            items_in_cart = cart_items.find_elements(By.CLASS_NAME, "product-name")
            self.assertTrue(any("Book1" in item.text for item in items_in_cart), "Expected product not found in cart")
        except Exception as e:
            self.fail(f"Shopping cart verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()