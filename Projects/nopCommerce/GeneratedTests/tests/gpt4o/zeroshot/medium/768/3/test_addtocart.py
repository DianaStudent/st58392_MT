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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 2: Click on the "Search" link in the top navigation.
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        self.assertIsNotNone(search_link, "Search link is not found on the homepage.")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        self.assertIsNotNone(search_input, "Search input box is not found on the search page.")
        search_input.send_keys("book")

        search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
        self.assertIsNotNone(search_button, "Search button is not found on the search page.")
        search_button.click()
        
        # Step 4: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-box-add-to-cart-button")))
        self.assertIsNotNone(add_to_cart_button, "Add to cart button is not found for the first product.")
        add_to_cart_button.click()
        
        # Step 5: Wait for the success notification to appear.
        notification = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        self.assertIsNotNone(notification, "Success notification did not appear.")
        
        # Step 6: Click the "shopping cart" link inside the notification.
        cart_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        self.assertIsNotNone(cart_link, "Shopping cart link is not found in the success notification.")
        cart_link.click()
        
        # Step 7: Confirm success by checking that the cart page contains the added product.
        cart_items = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart .product-name")))
        self.assertTrue(any("Book1" in item.text for item in cart_items), "Added product is not found in the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()