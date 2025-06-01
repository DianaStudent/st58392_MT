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

        # Search for a book
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Add the first book to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
        except:
            self.fail("Add to cart button not found")

        add_to_cart_button.click()

        # Check for success notification
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            self.assertTrue(success_notification.is_displayed(), "Success notification is not displayed")
            self.assertIn("shopping cart", success_notification.text, "Success notification does not contain cart link")
        except:
            self.fail("Success notification not found or doesn't contain cart link")

        # Check if the cart contains at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']/div[@class='count']/a[@href='/cart']"))
            )
            self.assertTrue("1 item(s)" in cart_count.text, "Cart is empty")
        except:
            self.fail("Cart is empty or cart count element not found")

if __name__ == "__main__":
    unittest.main()