from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Click on the "Search" link in the top navigation.
        search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search.
        search_input = self.wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")
        
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-button")))
        search_button.click()

        # Step 3: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: Wait for the success notification to appear.
        notification = self.wait.until(EC.presence_of_element_located((By.ID, "bar-notification")))
        self.assertTrue("The product has been added to your shopping cart" in notification.text)

        # Step 5: Click the "shopping cart" link inside the notification.
        cart_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 6: Confirm success by checking that the cart page contains the added product.
        cart_items = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart .product-name")))
        self.assertTrue(cart_items is not None and cart_items.text.strip() != "", "Cart does not contain the expected product.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()