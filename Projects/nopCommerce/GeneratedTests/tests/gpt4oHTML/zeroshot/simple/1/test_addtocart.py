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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Navigate to the home page
        driver.get("http://example.com")  # Replace with the actual URL

        # Check and search for a book using the search box
        try:
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        except:
            self.fail("Search elements not found")
        
        search_box.send_keys("book")
        search_button.click()

        # Wait for search results page and add the first book to the cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found on search results page")

        add_to_cart_button.click()

        # Check that the success notification is visible and check the cart link
        try:
            notification = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
            )
            cart_link = notification.find_element(By.TAG_NAME, "a")
        except:
            self.fail("Success notification or cart link not found")

        cart_link.click()

        # Verify that the cart contains at least one item
        try:
            cart_item_count = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mini-shopping-cart .items .item"))
            )
        except:
            self.fail("Cart does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()