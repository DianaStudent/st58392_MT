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
        self.base_url = "http://max/"
        self.search_term = "book"

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Navigate to the homepage.
        home_page_title = driver.title
        self.assertTrue(home_page_title is not None and home_page_title != "", "Home page title is missing or empty")

        # 2. Click on "Search" from the main menu.
        search_link_locator = (By.LINK_TEXT, "Search")
        search_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_link_locator))
        search_link.click()

        # 3. Type the search term "book" into the search field.
        search_field_locator = (By.ID, "q")
        search_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_field_locator))
        search_field.send_keys(self.search_term)

        # 4. Submit the search.
        search_button_locator = (By.CLASS_NAME, "button-1.search-button")
        search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_button_locator))
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(product_grid_locator))

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button_locator = (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")
        add_to_cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button_locator))
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_locator = (By.ID, "bar-notification")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(notification_locator))
        notification_element = driver.find_element(*notification_locator)
        self.assertTrue(notification_element.is_displayed(), "Notification bar is not visible")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link_locator = (By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']")
        shopping_cart_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(shopping_cart_link_locator))
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table_locator = (By.CLASS_NAME, "cart")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(cart_table_locator))

        cart_items_count_locator = (By.XPATH, "//div[@class='mini-shopping-cart']//a[contains(text(), 'item(s)')]")
        cart_items_count_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(cart_items_count_locator))
        cart_items_count_text = cart_items_count_element.text
        self.assertTrue("1 item(s)" in cart_items_count_text, "Cart does not contain at least one item")

if __name__ == "__main__":
    unittest.main()