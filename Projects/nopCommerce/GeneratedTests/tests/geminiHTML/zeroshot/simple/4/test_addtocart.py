import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
            search_box.send_keys("book")
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            self.fail(f"Search box not found or unable to enter text: {e}")

        # Add the first book to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or unable to click: {e}")

        # Verify success notification
        try:
            success_notification = wait.until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            self.assertTrue("The product has been added to your" in success_notification.text,
                            "Success notification text is incorrect")
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(cart_link.is_displayed(), "Cart link in notification is not displayed")
        except Exception as e:
            self.fail(f"Success notification not found or incorrect: {e}")

        # Verify that the cart contains at least one item
        try:
            mini_shopping_cart = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "mini-shopping-cart"))
            )
            count_element = mini_shopping_cart.find_element(By.CLASS_NAME, "count")
            self.assertTrue("There are" in count_element.text, "Cart count is incorrect")
        except Exception as e:
            self.fail(f"Cart count element not found or incorrect: {e}")


if __name__ == "__main__":
    unittest.main()