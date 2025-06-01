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
        self.driver.get("http://localhost/home")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_add_to_cart(self):
        driver = self.driver

        # Step 2: Click on "Search" from the main menu
        search_menu_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile li a[href='/search']")))
        search_menu_link.click()

        # Step 3: Type the search term "book" into the search field
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#small-searchterms")))
        search_input.clear()
        search_input.send_keys("book")

        # Step 4: Submit the search
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
        search_button.click()

        # Step 5: Wait for the product grid to load
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-container")))

        # Step 6: Locate the first product result and click the "Add to cart" button
        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "div.item-box div.buttons button.product-box-add-to-cart-button")
        add_to_cart_button.click()

        # Step 7: Wait for the notification bar to appear
        notification_bar = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))
        notification_text = notification_bar.text
        self.assertTrue("The product has been added to your shopping cart." in notification_text)

        # Verify the presence of the shopping cart link in the notification
        cart_link = notification_bar.find_element(By.PARTIAL_LINK_TEXT, "shopping cart")
        self.assertTrue(cart_link.is_displayed() and cart_link.get_attribute('href'))

        # Step 8: From the notification, click the "shopping cart" link
        cart_link.click()

        # Step 9: On the cart page, verify that the expected product is present
        cart_count = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mini-shopping-cart div.count a")))
        items_text = cart_count.text
        self.assertIn("1 item(s)", items_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()