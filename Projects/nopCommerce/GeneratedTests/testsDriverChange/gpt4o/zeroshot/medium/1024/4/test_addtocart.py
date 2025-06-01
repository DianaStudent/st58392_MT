import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 2: Click on the "Search" link in the top navigation.
        search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_field = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_field.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        search_button.click()

        # Step 4: On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.products-container > div.item-box:first-of-type button.product-box-add-to-cart-button")
        ))
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear.
        notification = self.wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        self.assertIn("The product has been added to your shopping cart", notification.text)

        # Step 6: Click the "shopping cart" link inside the notification.
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart contains at least one item.
        cart_count = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#flyout-cart .count a")))
        self.assertTrue(cart_count.text, "1 item(s)")

        cart_table = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart tbody tr")))
        product_name = cart_table.find_element(By.CLASS_NAME, "product-name")
        self.assertEqual(product_name.text, "Book1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()