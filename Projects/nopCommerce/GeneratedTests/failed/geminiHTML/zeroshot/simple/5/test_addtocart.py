from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a book
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search box or button not found")

        search_box.send_keys("book")
        search_button.click()

        # Add the first book to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Verify success notification
        try:
            success_notification = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            cart_link = success_notification.find_element(By.TAG_NAME, "a")
            self.assertEqual(cart_link.get_attribute("href"), "http://max/cart")
        except:
            self.fail("Success notification or cart link not found")

        # Verify item in cart
        try:
            mini_shopping_cart = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "mini-shopping-cart"))
            )
            item_count = mini_shopping_cart.find_element(By.CLASS_NAME, "count")
            self.assertIn("1 item(s)", item_count.text)
        except:
            self.fail("Cart item count not found or incorrect")

if __name__ == "__main__":
    unittest.main()