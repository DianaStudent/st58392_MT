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
                EC.element_to_be_clickable((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {e}")

        # Verify success notification
        try:
            notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            self.assertTrue(notification.is_displayed(), "Success notification is not displayed")
            self.assertIn("shopping cart", notification.text, "Success notification does not contain cart link")
        except Exception as e:
            self.fail(f"Success notification verification failed: {e}")

        # Verify that the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']/div[@class='count']/a"))
            )
            self.assertIn("1 item(s)", cart_count.text, "Cart does not contain at least one item")
        except:
            cart_count = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']/div[@class='count']"))
            )
            self.assertIn("1 item(s)", cart_count.text, "Cart does not contain at least one item")

if __name__ == "__main__":
    unittest.main()