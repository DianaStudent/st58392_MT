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
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys(self.search_term)

        # 4. Submit the search.
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-box-button"))
        )
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "bar-notification"))
        )

        try:
            # Locate the content within the notification bar
            notification_content = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//p[@class='content']"))
            )
            notification_text = notification_content.text
            self.assertTrue("The product has been added to your shopping cart" in notification_text,
                            f"Expected notification text not found. Actual text: {notification_text}")
        except Exception as e:
            self.fail(f"Notification bar text not found or incorrect: {e}")

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        product_name_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Book1"))
        )

        self.assertTrue("Book1" in product_name_element.text, "Expected product not found in cart.")

if __name__ == "__main__":
    unittest.main()