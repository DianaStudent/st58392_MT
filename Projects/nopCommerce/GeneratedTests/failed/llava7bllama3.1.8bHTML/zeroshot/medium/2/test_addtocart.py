from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart(self):
        self.driver.get("http://max/")  # Replace with actual homepage URL

        # Step 1: Click on the "Search" link in the top navigation
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "search_term")))
        search_field.send_keys("book")
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        search_button.click()

        # Step 3: On the search results page, locate the first product and click "Add to cart"
        product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='product-link'])[1]")))
        product_link.click()
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart']")))
        add_to_cart_button.click()

        # Step 4: Wait for the success notification to appear
        success_notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-notification']")))

        # Step 5: Click the "shopping cart" link inside the notification
        shopping_cart_link = WebDriverWait(success_notification, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping Cart")))
        shopping_cart_link.click()

        # Step 6: Confirm success by checking that the cart page contains the added product
        cart_page_title = self.driver.title
        if "Cart" not in cart_page_title:
            self.fail("Cart page title is incorrect")

        cart_contents = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "cart-contents")))
        if cart_contents.text.strip() == "":
            self.fail("Cart contents are empty")

if __name__ == "__main__":
    unittest.main()