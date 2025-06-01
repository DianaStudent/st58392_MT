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
        # 1. Navigate to the homepage. (Done in setUp)

        # 2. Click on "Search" from the main menu.
        search_link_locator = (By.LINK_TEXT, "Search")
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(search_link_locator)
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Search link not found or not clickable: {e}")

        # 3. Type the search term "book" into the search field.
        search_field_locator = (By.ID, "small-searchterms")
        try:
            search_field = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(search_field_locator)
            )
            search_field.send_keys("book")
        except Exception as e:
            self.fail(f"Search field not found or not interactable: {e}")

        # 4. Submit the search.
        search_button_locator = (By.CLASS_NAME, "button-1.search-box-button")
        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found or not clickable: {e}")

        # 5. Wait for the product grid to load.
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(product_grid_locator)
            )
        except Exception as e:
            self.fail(f"Product grid not found: {e}")

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button_locator = (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button_locator)
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {e}")

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar_locator = (By.ID, "bar-notification")
        try:
            notification_bar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(notification_bar_locator)
            )
            notification_text = notification_bar.text
            self.assertIn("The product has been added to your shopping cart", notification_text, "Notification message is incorrect.")
        except Exception as e:
            self.fail(f"Notification bar not found or incorrect text: {e}")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link_locator = (By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']")
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(shopping_cart_link_locator)
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Shopping cart link in notification not found or not clickable: {e}")

        # 9. On the cart page, verify that the expected product is present.
        cart_table_locator = (By.CLASS_NAME, "cart")
        try:
            cart_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(cart_table_locator)
            )
        except Exception as e:
            self.fail(f"Cart table not found: {e}")

        product_name_locator = (By.LINK_TEXT, "Book1")
        try:
            product_name_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(product_name_locator)
            )
            self.assertTrue(product_name_element.is_displayed(), "Product 'Book1' is not displayed in the cart.")
        except Exception as e:
            self.fail(f"Product name 'Book1' not found in cart: {e}")

if __name__ == "__main__":
    unittest.main()