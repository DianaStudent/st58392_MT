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
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")

        # 4. Submit the search.
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        notification_text = notification_bar.text
        if not notification_text:
            self.fail("Notification text is empty.")
        expected_notification_text = "The product has been added to your shopping cart"
        if expected_notification_text not in notification_text:
            self.fail(f"Expected notification text '{expected_notification_text}' not found in '{notification_text}'")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']")))
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        if not cart_table:
            self.fail("Cart table not found.")

        product_name_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
        product_name = product_name_element.text
        if not product_name:
            self.fail("Product name not found in cart.")

        # Confirm success by checking that the cart contains at least one item.
        cart_count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']/div[@class='count']/a")))
        cart_count_text = cart_count_element.text
        if not cart_count_text:
            self.fail("Cart count text is empty.")
        if "1 item(s)" not in cart_count_text:
            self.fail("Cart does not contain at least one item.")

if __name__ == "__main__":
    unittest.main()