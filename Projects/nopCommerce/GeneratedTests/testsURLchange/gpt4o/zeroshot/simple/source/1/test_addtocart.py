import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCartProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Search for a book
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_box.send_keys("book")

        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        search_button.click()

        # Wait for search results
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results .product-grid"))
        )

        # Add the first product to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Check for success notification
        success_notification = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification .success"))
        )
        self.assertIn("The product has been added to your shopping cart", success_notification.text)

        # Confirm cart contains at least one item
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#bar-notification a[href='/cart']"))
        )
        cart_link.click()

        cart_count = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flyout-cart .count a"))
        )

        cart_text = cart_count.text
        if "1 item(s)" not in cart_text:
            self.fail(f"Cart does not contain the expected number of items. Found: {cart_text}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()