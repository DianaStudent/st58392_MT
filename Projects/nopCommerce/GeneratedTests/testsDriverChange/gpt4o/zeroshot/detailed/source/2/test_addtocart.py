import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 2: Click on "Search" from the main menu.
        search_menu_item = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_menu_item.click()

        # Step 3: Type the search term "book" into the search field.
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_field.send_keys("book")

        # Step 4: Submit the search.
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Step 5: Wait for the product grid to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper"))
        )

        # Step 6: Locate the first product result and click the "Add to cart" button.
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "product-box-add-to-cart-button")
        if not add_to_cart_buttons:
            self.fail("Add to cart button not found.")
        add_to_cart_buttons[0].click()

        # Step 7: Wait for the notification bar to appear.
        notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )
        self.assertIn("The product has been added to your shopping cart", notification.text)

        # Step 8: From the notification, click the "shopping cart" link.
        cart_link = notification.find_element(By.TAG_NAME, "a")
        if not cart_link:
            self.fail("Shopping cart link in notification not found.")
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present.
        cart_items = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )
        if not cart_items.text:
            self.fail("Cart is empty.")
        self.assertIn("Book1", cart_items.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()