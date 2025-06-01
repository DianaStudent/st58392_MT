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
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
            )
            self.assertTrue("The product has been added to your shopping cart" in success_notification.text)

            # Check for the cart link in the notification
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertIsNotNone(cart_link)

        except Exception as e:
            self.fail(f"Success notification verification failed: {e}")

        # Verify that the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']/div[@class='count']/a[contains(text(), 'item(s)')]"))
            )
            self.assertTrue("1 item(s)" in cart_count.text)
        except Exception as e:
            self.fail(f"Cart verification failed: {e}")

if __name__ == "__main__":
    unittest.main()