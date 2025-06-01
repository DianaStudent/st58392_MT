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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Navigate to the homepage.
        driver.get("http://max/")

        # Step 2: Click on "Search" from the main menu.
        search_menu_selector = (By.XPATH, "//a[@href='/search']")
        search_menu = wait.until(EC.presence_of_element_located(search_menu_selector))
        search_menu.click()

        # Step 3: Type the search term "book" into the search field.
        search_field_selector = (By.ID, "q")
        search_field = wait.until(EC.presence_of_element_located(search_field_selector))
        search_field.clear()
        search_field.send_keys("book")

        # Step 4: Submit the search.
        search_button_selector = (By.XPATH, "//button[@class='button-1 search-button']")
        search_button = wait.until(EC.presence_of_element_located(search_button_selector))
        search_button.click()

        # Step 5: Wait for the product grid to load.
        product_grid_selector = (By.CLASS_NAME, "product-grid")
        wait.until(EC.presence_of_element_located(product_grid_selector))

        # Step 6: Locate the first product result and click the "Add to cart" button.
        add_to_cart_button_selector = (By.XPATH, "(//button[@class='button-2 product-box-add-to-cart-button'])[1]")
        add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_button_selector))
        add_to_cart_button.click()

        # Step 7: Wait for the notification bar to appear.
        notification_selector = (By.ID, "bar-notification")
        notification = wait.until(EC.visibility_of_element_located(notification_selector))
        self.assertTrue(notification.is_displayed(), "Notification is not visible")
        self.assertIn("shopping cart", notification.text, "Notification does not contain expected link to shopping cart")

        # Step 8: From the notification, click the "shopping cart" link.
        cart_link_selector = (By.XPATH, "//a[@href='/cart']")
        cart_link = wait.until(EC.presence_of_element_located(cart_link_selector))
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present.
        cart_product_selector = (By.XPATH, "//td[@class='product']/a[text()='Book1']")
        cart_product = wait.until(EC.presence_of_element_located(cart_product_selector))
        self.assertTrue(cart_product.is_displayed(), "Expected product is not present in cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()