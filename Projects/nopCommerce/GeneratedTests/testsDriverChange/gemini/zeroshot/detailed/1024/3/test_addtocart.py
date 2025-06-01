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
        search_link.click()

        # 3. Type the search term "book" into the search field.
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys(self.search_term)

        # 4. Submit the search.
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-button"))
        )
        search_button.click()

        # 5. Wait for the product grid to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "bar-notification"))
        )
        notification_text = notification_bar.text

        if not notification_text:
            self.fail("Notification text is empty.")

        expected_notification_text_part = "The product has been added to your shopping cart"
        self.assertTrue(expected_notification_text_part in notification_text,
                        f"Expected '{expected_notification_text_part}' in notification text, but got '{notification_text}'")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        if not cart_table:
            self.fail("Cart table not found.")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
        self.assertGreater(len(cart_items), 0, "Cart is empty.")

        product_name_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Book1"))
        )
        product_name = product_name_element.text

        if not product_name:
            self.fail("Product name is empty.")

        self.assertEqual(product_name, "Book1", "Incorrect product in cart.")


if __name__ == "__main__":
    unittest.main()