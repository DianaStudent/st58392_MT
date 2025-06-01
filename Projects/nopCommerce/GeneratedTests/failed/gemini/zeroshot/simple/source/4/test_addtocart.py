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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Search for a book
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search box or button not found")

        search_box.send_keys("book")
        search_button.click()

        # Add the first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found")

        add_to_cart_button.click()

        # Check for the success notification
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(success_notification.is_displayed(), "Success notification is not displayed")
            self.assertIn("shopping cart", success_notification.text, "Success notification does not contain cart link")
        except:
            self.fail("Success notification not found or does not contain cart link")

        # Check that the cart contains at least one item
        try:
            mini_shopping_cart = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "mini-shopping-cart"))
            )
            cart_count = mini_shopping_cart.find_element(By.CLASS_NAME, "count")
            self.assertIn("1 item(s)", cart_count.text, "Cart does not contain at least one item")
        except:
            self.fail("Cart count not found or cart is empty")

if __name__ == "__main__":
    unittest.main()