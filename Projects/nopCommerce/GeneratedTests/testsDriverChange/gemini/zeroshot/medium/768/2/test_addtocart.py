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
        wait = WebDriverWait(driver, 20)

        # 1. Click on the "Search" link in the top navigation.
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found")

        # 2. Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if search_input:
            search_input.send_keys("book")
        else:
            self.fail("Search input field not found")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button")))
        if search_button:
            search_button.click()
        else:
            self.fail("Search button not found")

        # 3. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")

        # 4. Wait for the success notification to appear.
        success_notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        if not success_notification:
            self.fail("Success notification not found")

        # 5. Click the "shopping cart" link inside the notification.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']")))
        if shopping_cart_link:
            shopping_cart_link.click()
        else:
            self.fail("Shopping cart link in notification not found")

        # 6. Confirm success by checking that the cart page contains the added product.
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        if not cart_table:
            self.fail("Cart table not found")

        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
        if len(cart_items) == 0:
            self.fail("No items found in the cart")

if __name__ == "__main__":
    unittest.main()