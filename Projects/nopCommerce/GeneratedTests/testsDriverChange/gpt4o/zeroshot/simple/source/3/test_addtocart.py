import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a book
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
        except:
            self.fail("Search box not found.")
        
        search_box.send_keys('book')

        try:
            search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.search-box-button')))
        except:
            self.fail("Search button not found.")
        
        search_button.click()

        # Add the first book to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-box-add-to-cart-button')))
        except:
            self.fail("Add to cart button not found.")
        
        add_to_cart_button.click()

        # Verify if product is added to cart
        try:
            success_notification = wait.until(EC.visibility_of_element_located((By.ID, 'bar-notification')))
        except:
            self.fail("Success notification not displayed.")
        
        self.assertIn("The product has been added to your shopping cart", success_notification.text)

        try:
            cart_link = success_notification.find_element(By.TAG_NAME, 'a')
        except:
            self.fail("Cart link not found in success notification.")
        
        cart_link.click()

        # Confirm cart has at least one item
        try:
            cart_item_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.count a')))
        except:
            self.fail("Cart item count not found.")
        
        items_text = cart_item_count.text
        self.assertTrue(int(items_text.split()[0]) >= 1, "Cart does not contain at least one item.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()