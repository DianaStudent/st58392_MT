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
        except:
            self.fail("Search box not found")

        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except:
            self.fail("Search button not found or not clickable")

        # Add the first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Check for success notification
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            self.assertTrue("The product has been added to your" in success_notification.text, "Success notification text is incorrect")
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(cart_link.is_displayed(), "Cart link in success notification is not displayed")

        except:
            self.fail("Success notification not found or incorrect")

        # Check that the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='flyout-cart']//div[@class='count']/a"))
            )
            self.assertTrue("1 item(s)" in cart_count.text, "Cart count is incorrect")
        except:
             try:
                cart_count = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@id='flyout-cart']//div[@class='count']"))
                )
                self.assertTrue("There are 1 item(s)" in cart_count.text, "Cart count is incorrect")
             except:
                self.fail("Cart is empty or count element not found")

if __name__ == "__main__":
    unittest.main()