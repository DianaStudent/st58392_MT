from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Assuming base URL here, provide the actual if known

    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Locate the search box and search for the keyword 'book'
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book" + Keys.RETURN)
        except Exception as e:
            self.fail("Search box not found or could not perform search: " + str(e))

        # Wait for the search results and find the 'Add to cart' button for the first item
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button not found or could not be clicked: " + str(e))

        # Validate success notification and cart link
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success .content"))
            )
            self.assertIn("The product has been added to your shopping cart", success_notification.text)
            cart_link = success_notification.find_element(By.XPATH, ".//a[@href='/cart']")
            cart_link.click()
        except Exception as e:
            self.fail("Success notification not visible or does not contain correct link: " + str(e))
        
        # Verify that cart contains at least one item
        try:
            cart_item_count = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-shopping-cart .count a"))
            )
            self.assertTrue("1 item" in cart_item_count.text)
        except Exception as e:
            self.fail("Cart item count verification failed: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()