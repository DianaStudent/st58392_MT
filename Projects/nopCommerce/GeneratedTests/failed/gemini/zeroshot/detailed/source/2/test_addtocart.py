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

        # 1. Navigate to the homepage. (Done in setUp)

        # 2. Click on "Search" from the main menu.
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # 3. Type the search term "book" into the search field.
        search_field = wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_field.send_keys("book")

        # 4. Submit the search.
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = wait.until(EC.presence_of_element_located((By.ID, "bar-notification")))
        notification_text = notification_bar.find_element(By.CLASS_NAME, "content").text
        if not notification_text:
            self.fail("Notification text is empty.")
        self.assertIn("The product has been added to your shopping cart", notification_text)

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        cart_items = cart_table.find_elements(By.TAG_NAME, "tr")
        if len(cart_items) <= 1:
            self.fail("Cart is empty.")

        product_name_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
        product_name = product_name_element.text
        if not product_name:
            self.fail("Product name is empty.")
        self.assertIn("Book1", product_name)

if __name__ == "__main__":
    unittest.main()