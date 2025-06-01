import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Step 1: Open the homepage.
        driver.get("http://example-homepage-url")
        
        # Step 2: Click on the "Search" link in the top navigation.
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link is missing.")
        search_link.click()
        
        # Step 3: Enter "book" in the search field and submit the search.
        search_field = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_field:
            self.fail("Search field is missing.")
        search_field.send_keys("book")
        
        search_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 search-button']")))
        if not search_button:
            self.fail("Search button is missing.")
        search_button.click()
        
        # Step 4: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@class='button-2 product-box-add-to-cart-button'])[1]")))
        if not add_to_cart_button:
            self.fail("Add to cart button is missing.")
        add_to_cart_button.click()
        
        # Step 5: Wait for the success notification to appear.
        success_notification = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bar-notification")))
        if not success_notification:
            self.fail("Success notification did not appear.")
        
        # Ensure that the success notification is visible and contains a link to the cart.
        notification_text = success_notification.find_element(By.TAG_NAME, "p").text
        if "The product has been added to your shopping cart" not in notification_text:
            self.fail("Success notification text is incorrect.")
        
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Shopping cart link is missing in notification.")
        cart_link.click()
        
        # Step 6: Confirm success by checking that the cart page contains the added product.
        cart_summary = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-summary-content")))
        if not cart_summary:
            self.fail("Cart summary content is missing.")
        
        cart_items = self.wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='cart']//tr[td[@class='product']]")))
        if not cart_items:
            self.fail("Cart does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()