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

        # 1. Navigate to the homepage. (Done in setUp)

        # 2. Click on "Search" from the main menu.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Type the search term "book" into the search field.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if search_input:
            search_input.send_keys("book")
        else:
            self.fail("Search input field not found.")

        # 4. Submit the search.
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-button")))
        if search_button:
            search_button.click()
        else:
            self.fail("Search button not found.")

        # 5. Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        if not product_grid:
            self.fail("Product grid not found.")

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = wait.until(EC.presence_of_element_located((By.ID, "bar-notification")))
        if not notification_bar:
            self.fail("Notification bar not found.")

        notification_text = notification_bar.find_element(By.CLASS_NAME, "content").text
        if not notification_text or "The product has been added to your shopping cart" not in notification_text:
            self.fail("Notification text is incorrect or empty.")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 9. On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        if not cart_table:
            self.fail("Cart table not found.")

        product_name_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Book1")))

        if not product_name_element:
            self.fail("Product 'Book1' not found in cart.")

if __name__ == "__main__":
    unittest.main()