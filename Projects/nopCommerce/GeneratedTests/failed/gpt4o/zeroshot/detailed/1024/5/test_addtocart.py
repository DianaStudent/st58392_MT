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
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the Search page
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        self.assertTrue(search_link.is_displayed())
        search_link.click()

        # Type 'book' into the search field and submit
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.clear()
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Wait for the product grid to load and locate the first product
        product_add_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        self.assertIsNotNone(product_add_button)
        product_add_button.click()

        # Verify success notification appears
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        self.assertTrue(notification.is_displayed())
        notification_text = notification.find_element(By.CLASS_NAME, "content").text
        self.assertIn("The product has been added to your shopping cart", notification_text)

        # Click the "shopping cart" link in the notification
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        self.assertTrue(cart_link.is_displayed())
        cart_link.click()

        # Verify the cart page contains the expected product
        cart_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-name")))
        self.assertTrue(cart_product.is_displayed())
        cart_product_text = cart_product.text
        self.assertEqual(cart_product_text, "Book1")

        # Verify there's at least one item in the cart
        cart_count = driver.find_element(By.CSS_SELECTOR, ".count a").text
        self.assertIn("1 item(s)", cart_count)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()