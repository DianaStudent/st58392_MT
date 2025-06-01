import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click on the "Search" link in the top navigation.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        if search_field:
            search_field.send_keys("book")
        else:
            self.fail("Search field not found.")

        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-box-button"))
        )

        if search_button:
            search_button.click()
        else:
            self.fail("Search button not found.")

        # 4. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button"))
        )
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Wait for the success notification to appear.
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )

        if not success_notification:
            self.fail("Success notification not found.")

        # 6. Click the "shopping cart" link inside the notification.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )
        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found.")

        # 7. Confirm success by checking that the cart page contains the added product.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        if not cart_table:
            self.fail("Cart table not found.")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")

        if not cart_items:
            self.fail("No items found in cart.")

        self.assertTrue(len(cart_items) > 0, "Cart is empty.")

if __name__ == "__main__":
    unittest.main()