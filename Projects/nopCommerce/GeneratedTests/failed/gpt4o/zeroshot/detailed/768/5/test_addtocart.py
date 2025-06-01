from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Navigate to the homepage
        self.assertIn("nopCommerce", driver.title)

        # 2. Click on "Search" from the main menu
        search_menu = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_menu.click()

        # 3. Type the search term "book" into the search field
        search_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search-text"))
        )
        search_box.send_keys("book")

        # 4. Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # 5. Wait for the product grid to load
        product_grid = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.item-grid"))
        )

        # 6. Locate the first product result and click the "Add to cart" button
        add_to_cart_button = product_grid.find_element(By.CSS_SELECTOR, "button.product-box-add-to-cart-button")
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear
        notification_bar = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success"))
        )
        self.assertIn("The product has been added to your shopping cart", notification_bar.text)

        # 8. From the notification, click the "shopping cart" link
        cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # 9. On the cart page, verify that the expected product is present
        cart_item = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart"))
        )
        product_name = cart_item.find_element(By.LINK_TEXT, "Book1")
        self.assertEqual(product_name.text, "Book1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()