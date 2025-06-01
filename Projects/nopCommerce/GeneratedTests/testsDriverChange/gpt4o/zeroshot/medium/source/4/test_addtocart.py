import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Click on the "Search" link in the top navigation.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Search')))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        search_input.send_keys('book')
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 search-button']")))
        search_button.click()

        # Step 3: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='button-2 product-box-add-to-cart-button'])[1]")))
        add_to_cart_button.click()

        # Step 4: Wait for the success notification to appear.
        notification = wait.until(EC.visibility_of_element_located((By.ID, 'bar-notification')))
        self.assertTrue(notification.is_displayed(), "Notification is not displayed")
        
        # Check the notification has the link to the cart
        cart_link = notification.find_element(By.LINK_TEXT, 'shopping cart')
        self.assertTrue(cart_link.is_displayed(), "Cart link is not displayed in the notification")

        # Step 5: Click the "shopping cart" link inside the notification.
        cart_link.click()

        # Step 6: Confirm success by checking that the cart page contains the added product.
        cart_item_count = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='count']//a")))
        item_count_text = cart_item_count.text
        self.assertTrue(item_count_text, "Cart is empty")
        self.assertIn('1 item(s)', item_count_text, "Incorrect item count in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()