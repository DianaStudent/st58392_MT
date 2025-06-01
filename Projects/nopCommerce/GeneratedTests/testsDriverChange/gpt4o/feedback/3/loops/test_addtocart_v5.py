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

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Wait for the homepage to load and click on the "Search" link
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Enter the search term "book"
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys("book")

        # Submit the search form
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        if not search_button:
            self.fail("Search button not found.")
        search_button.click()

        # Wait for the product grid to load
        product_buttons = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        
        if not product_buttons:
            self.fail("No products found to add to the cart.")
        
        # Click on "Add to cart" button for the first product
        product_buttons[0].click()

        # Wait for the notification bar to appear
        notification_bar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )

        # Check if notification bar contains the link to cart
        notification_text = notification_bar.find_element(By.CSS_SELECTOR, ".content").text
        self.assertIn("The product has been added to your shopping cart", notification_text)

        # Click on the "shopping cart" link in the notification
        cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Shopping cart link not found in notification.")
        cart_link.click()

        # Verify that the shopping cart contains at least one item
        cart_items = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart tbody tr"))
        )
        
        if not cart_items:
            self.fail("Cart is empty when it should contain at least one item.")

if __name__ == "__main__":
    unittest.main()