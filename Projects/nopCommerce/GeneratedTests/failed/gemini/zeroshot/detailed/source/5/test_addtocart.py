from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Navigate to the homepage.
        # Already done in setUp

        # 2. Click on "Search" from the main menu.
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Type the search term "book" into the search field.
        search_input_field = wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        if search_input_field:
            search_input_field.send_keys("book")
        else:
            self.fail("Search input field not found.")

        # 4. Submit the search.
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-box-button")))
        if search_button:
            search_button.click()
        else:
            self.fail("Search button not found.")

        # 5. Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        if not product_grid:
            self.fail("Product grid did not load.")

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = wait.until(EC.presence_of_element_located((By.ID, "bar-notification")))
        if not notification_bar:
            self.fail("Notification bar did not appear.")

        notification_text = notification_bar.text
        if not notification_text or "The product has been added to your shopping cart" not in notification_text:
            self.fail("Incorrect notification message: " + (notification_text if notification_text else "Notification text is empty"))

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 9. On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        if not cart_table:
            self.fail("Cart table not found.")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
        if not cart_items or len(cart_items) == 0:
            self.fail("No items found in the cart.")

        product_name_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Book1")))
        if not product_name_element:
            self.fail("Book1 not found in cart")

if __name__ == "__main__":
    unittest.main()