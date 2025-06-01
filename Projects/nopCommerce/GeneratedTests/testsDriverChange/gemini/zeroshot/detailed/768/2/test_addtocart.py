import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Navigate to the homepage. (Done in setUp)

        # 2. Click on "Search" from the main menu.
        try:
            search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found in the main menu.")

        # 3. Type the search term "book" into the search field.
        try:
            search_field = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_field.send_keys("book")
        except NoSuchElementException:
            self.fail("Search input field not found.")

        # 4. Submit the search.
        try:
            search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-box-button")))
            search_button.click()
        except NoSuchElementException:
            self.fail("Search button not found.")

        # 5. Wait for the product grid to load.
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        except NoSuchElementException:
            self.fail("Product grid did not load.")

        # 6. Locate the first product result and click the "Add to cart" button.
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button")))
            add_to_cart_button.click()
        except NoSuchElementException:
            self.fail("Add to cart button not found for the first product.")

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        try:
            notification_bar = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
            notification_text = notification_bar.find_element(By.CLASS_NAME, "content").text
            self.assertTrue("The product has been added to your shopping cart" in notification_text, "Notification message is incorrect.")
        except NoSuchElementException:
            self.fail("Notification bar did not appear.")

        # 8. From the notification, click the "shopping cart" link.
        try:
            shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
            shopping_cart_link.click()
        except NoSuchElementException:
            self.fail("Shopping cart link not found in the notification bar.")

        # 9. On the cart page, verify that the expected product is present.
        try:
            cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
            product_name_element = cart_table.find_element(By.CLASS_NAME, "product-name")
            product_name = product_name_element.text
            self.assertTrue(product_name != "", "Product name is empty in the cart.")
            self.assertEqual(product_name, "Book1", "Incorrect product in cart.")
        except NoSuchElementException:
            self.fail("Product not found in the cart.")

if __name__ == "__main__":
    unittest.main()