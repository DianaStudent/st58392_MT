from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_input.send_keys("book")

        # 4. Submit the search.
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-box-button")))
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        notification_text = notification_bar.find_element(By.CLASS_NAME, "content").text

        if not notification_text:
            self.fail("Notification text is empty.")

        expected_notification_text_start = "The product has been added to your "
        if not notification_text.startswith(expected_notification_text_start):
            self.fail(f"Notification text does not start with expected text. Actual: {notification_text}")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        product_name_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
        product_name = product_name_element.text

        if not product_name:
            self.fail("Product name in cart is empty.")

        expected_product_name = "Book1"
        if product_name != expected_product_name:
            self.fail(f"Incorrect product in cart. Expected: {expected_product_name}, Actual: {product_name}")

        # Confirm success by checking that the cart contains at least one item.
        cart_count_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "count")))
        cart_count_text = cart_count_element.text

        if not cart_count_text:
            self.fail("Cart count text is empty.")

        if "no items" in cart_count_text.lower():
            self.fail("Cart is empty after adding product.")


if __name__ == "__main__":
    unittest.main()