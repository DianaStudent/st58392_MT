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
        home_page_title = driver.title
        if not home_page_title:
            self.fail("Home page title is missing.")

        # 2. Click on "Search" from the main menu.
        search_link_locator = (By.LINK_TEXT, "Search")
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(search_link_locator)
        )
        search_link.click()

        # 3. Type the search term "book" into the search field.
        search_field_locator = (By.ID, "small-searchterms")
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(search_field_locator)
        )
        search_field.send_keys(self.search_term)

        # 4. Submit the search.
        search_button_locator = (By.CLASS_NAME, "button-1.search-box-button")
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(search_button_locator)
        )
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(product_grid_locator)
        )

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button_locator = (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(add_to_cart_button_locator)
        )
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_locator = (By.ID, "bar-notification")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(notification_locator)
        )

        notification_content_locator = (By.CSS_SELECTOR, "#bar-notification .content")
        notification_content = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(notification_content_locator)
        )
        notification_text = notification_content.text
        if not notification_text:
            self.fail("Notification text is missing.")

        expected_notification_text_part = "The product has been added to your"
        if expected_notification_text_part not in notification_text:
            self.fail(f"Expected notification text part '{expected_notification_text_part}' not found in '{notification_text}'.")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link_locator = (By.LINK_TEXT, "shopping cart")
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(shopping_cart_link_locator)
        )
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_page_title_locator = (By.CLASS_NAME, "page-title")
        cart_page_title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(cart_page_title_locator)
        )

        cart_page_title_text = cart_page_title.find_element(By.TAG_NAME, "h1").text
        if not cart_page_title_text:
            self.fail("Cart page title is missing.")

        expected_cart_title = "Shopping cart"
        if expected_cart_title not in cart_page_title_text:
            self.fail(f"Expected cart title '{expected_cart_title}' not found in '{cart_page_title_text}'.")

        #Check that the cart contains at least one item.
        cart_table_locator = (By.CLASS_NAME, "cart")
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(cart_table_locator)
        )
        cart_rows = cart_table.find_elements(By.TAG_NAME, "tr")
        if len(cart_rows) <= 1:
            self.fail("Cart is empty.")


if __name__ == "__main__":
    unittest.main()