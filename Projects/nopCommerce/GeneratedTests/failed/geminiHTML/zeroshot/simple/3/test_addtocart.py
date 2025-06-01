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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_book_to_cart(self):
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
        except Exception as e:
            self.fail(f"Search box or button not found: {e}")

        search_box.send_keys("book")
        search_button.click()

        # Add the first book to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
        except Exception as e:
            self.fail(f"Add to cart button not found: {e}")

        add_to_cart_button.click()

        # Verify success notification
        try:
            success_notification = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(success_notification.is_displayed(), "Success notification is not displayed")
            self.assertEqual(cart_link.get_attribute("href"), "http://max/cart", "Cart link is incorrect")
        except Exception as e:
            self.fail(f"Success notification or cart link not found: {e}")

        # Verify that the cart contains at least one item
        try:
            mini_shopping_cart = wait.until(
                EC.presence_of_element_located((By.ID, "flyout-cart"))
            )
            cart_count = mini_shopping_cart.find_element(By.CLASS_NAME, "count")
            self.assertIn("1 item(s)", cart_count.text, "Cart does not contain at least one item")
        except Exception as e:
            self.fail(f"Cart count not found or incorrect: {e}")


if __name__ == "__main__":
    unittest.main()