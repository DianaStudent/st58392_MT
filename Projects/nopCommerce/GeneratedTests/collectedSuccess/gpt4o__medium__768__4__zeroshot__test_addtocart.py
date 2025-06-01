import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the "Search" link in the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found")

        search_link.click()

        # Step 2: Enter "book" in search field and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input field not found")

        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        if not search_button:
            self.fail("Search button not found")
        
        search_button.click()

        # Step 3: Locate the first product and click "Add to cart"
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")

        add_to_cart_button.click()

        # Step 4: Wait for success notification and confirm it contains a link to the cart
        success_notification = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "bar-notification.success")))
        if not success_notification:
            self.fail("Success notification not displayed")

        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Link to shopping cart not found in success notification")

        cart_link.click()

        # Step 5: Confirm the cart page contains the added product
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-total")))
        if not cart_items:
            self.fail("Cart is empty or cart item not found")

        product_name = driver.find_element(By.CLASS_NAME, "product-name")
        if not product_name or product_name.text.strip() == "":
            self.fail("Product name not found or is empty in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()