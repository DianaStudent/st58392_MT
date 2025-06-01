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
                EC.presence_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except:
            self.fail("Search button not found")

        # Add the first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Verify success notification
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification"))
            )
            self.assertTrue(success_notification.is_displayed(), "Success notification is not displayed")
            self.assertIn("The product has been added to your", success_notification.text, "Incorrect success message")
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(cart_link.is_displayed(), "Cart link in notification not found")
        except:
            self.fail("Success notification not found or incorrect")

        # Verify item in cart
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='flyout-cart']//div[@class='count']/a[@href='/cart']"))
            )
            self.assertIn("1 item(s)", cart_count.text, "Cart count is incorrect")
        except:
            self.fail("Cart count element not found or incorrect")

        # Navigate to cart page and verify item
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='flyout-cart']//div[@class='count']/a[@href='/cart']"))
            )
            cart_link.click()
        except:
            self.fail("Cart link not found")

        try:
            cart_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart"))
            )
            self.assertTrue(cart_table.is_displayed(), "Cart table not displayed")
            product_name = cart_table.find_element(By.CLASS_NAME, "product-name")
            self.assertTrue(product_name.is_displayed(), "Product name not displayed")
        except:
            self.fail("Cart table or product name not found")

if __name__ == "__main__":
    unittest.main()