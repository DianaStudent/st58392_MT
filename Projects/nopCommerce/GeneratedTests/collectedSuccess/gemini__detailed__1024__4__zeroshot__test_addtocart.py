import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.search_term = "book"

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Navigate to the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on "Search" from the main menu.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Type the search term "book" into the search field.
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        if search_input:
            search_input.send_keys(self.search_term)
        else:
            self.fail("Search input field not found.")

        # 4. Submit the search.
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-box-button"))
        )
        if search_button:
            search_button.click()
        else:
            self.fail("Search button not found.")

        # 5. Wait for the product grid to load.
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )
        if not product_grid:
            self.fail("Product grid did not load.")

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "bar-notification"))
        )
        if not notification_bar:
            self.fail("Notification bar did not appear.")

        notification_text_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#bar-notification .content"))
        )

        if not notification_text_element:
            self.fail("Notification text element not found.")

        notification_text = notification_text_element.text
        if not notification_text:
            self.fail("Notification text is empty.")

        expected_notification_text_part = "The product has been added to your"
        self.assertTrue(expected_notification_text_part in notification_text,
                            f"Expected '{expected_notification_text_part}' in notification text, but got '{notification_text}'")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#bar-notification .content a[href='/cart']"))
        )
        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 9. On the cart page, verify that the expected product is present.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )
        if not cart_table:
            self.fail("Cart table not found.")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
        if not cart_items:
            self.fail("No items found in the cart.")

        self.assertTrue(len(cart_items) > 0, "Cart is empty.")

if __name__ == "__main__":
    unittest.main()