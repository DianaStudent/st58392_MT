from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the homepage and click on the "Search" link in the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_field.send_keys("book")
        search_field.send_keys(Keys.RETURN)

        # On the search results page, locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Wait for the success notification to appear
        notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))

        # Confirm notification is present and it contains the cart link
        self.assertTrue(notification.is_displayed())
        
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Confirm success by checking that the cart contains the added product
        cart_item_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".count a")))
        self.assertIn("1 item(s)", cart_item_count.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()