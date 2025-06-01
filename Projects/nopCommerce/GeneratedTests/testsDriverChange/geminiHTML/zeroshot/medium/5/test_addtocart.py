import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Already done in setUp)

        # 2. Click on the "Search" link in the top navigation.
        search_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Enter "book" in the search field and submit the search.
        search_field = wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        if search_field:
            search_field.send_keys("book")
            search_field.send_keys(Keys.RETURN)
        else:
            self.fail("Search field not found.")

        # 4. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Wait for the success notification to appear.
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification.success"))
        )

        if not success_notification:
            self.fail("Success notification not found.")

        # 6. Click the "shopping cart" link inside the notification.
        shopping_cart_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))
        )

        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 7. Confirm success by checking that the cart page contains the added product.
        cart_table = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        if not cart_table:
            self.fail("Cart table not found.")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")

        if not cart_items:
            self.fail("No items found in the cart.")

        self.assertTrue(len(cart_items) > 0, "Cart is empty.")


if __name__ == "__main__":
    unittest.main()