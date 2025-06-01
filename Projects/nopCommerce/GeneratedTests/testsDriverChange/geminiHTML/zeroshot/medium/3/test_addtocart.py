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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.set_window_size(1200, 800)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click on the "Search" link in the top navigation.
        search_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
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
            search_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            if search_button:
                search_button.click()
            else:
                self.fail("Search button not found.")
        else:
            self.fail("Search field not found.")

        # 4. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Wait for the success notification to appear.
        success_notification = wait.until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )
        if not success_notification:
            self.fail("Success notification not found.")

        # 6. Click the "shopping cart" link inside the notification.
        shopping_cart_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )

        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 7. Confirm success by checking that the cart page contains the added product.
        cart_items = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@class='cart']//tbody//tr"))
        )

        if cart_items and len(cart_items) > 0:
            print("Successfully added to cart.")
        else:
            self.fail("No items found in the cart.")


if __name__ == "__main__":
    unittest.main()