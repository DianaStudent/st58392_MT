from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Search Page
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box is not found on the home page.")

        search_box.send_keys("book")

        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except:
            self.fail("Search button is not found on the home page.")
        
        # Find and click "Add to cart" for the first product
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button is not found or not clickable.")

        # Verify success notification
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            self.assertIn("The product has been added to your shopping cart", success_notification.text)
            cart_link = success_notification.find_element(By.TAG_NAME, "a")
            cart_link.click()
        except:
            self.fail("Success notification is not visible or does not contain the cart link.")

        # Confirm cart contains at least one item
        try:
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "count"))
            )
            self.assertIn("item(s)", cart_items.text)
        except:
            self.fail("The cart does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()