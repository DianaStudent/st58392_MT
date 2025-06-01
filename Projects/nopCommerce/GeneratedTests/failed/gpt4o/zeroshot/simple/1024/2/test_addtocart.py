from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Implicit wait as a backup
        self.base_url = "http://max/"

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)

        # Search for the book
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#small-searchterms"))
            )
        except:
            self.fail("Search box not found")

        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results and find the first "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found in search results")

        add_to_cart_button.click()

        # Verify success notification and presence of cart link
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
            )
            cart_link = success_notification.find_element(By.CSS_SELECTOR, "a[href='/cart']")
        except:
            self.fail("Success notification or cart link not found")

        # Verify that the cart contains at least one item
        driver.get(self.base_url + "cart")
        
        try:
            cart_items = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".mini-shopping-cart .count a[href='/cart']"))
            )
            self.assertIn("1 item(s)", cart_items.text)
        except:
            self.fail("Cart does not contain at least one item")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()