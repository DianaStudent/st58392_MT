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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_product_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the homepage
        driver.get('data:text/html;charset=utf-8,' + html_data["home"])

        # Click on "Search" from the main menu
        search_menu_item = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_menu_item.click()

        # Load the search page
        driver.get('data:text/html;charset=utf-8,' + html_data["search_page"])

        # Type the search term "book" into the search field
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        if not search_box:
            self.fail("Search box not found")
        search_box.send_keys("book")

        # Submit the search
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Load the search results page
        driver.get('data:text/html;charset=utf-8,' + html_data["search_results"])

        # Wait for the product grid to load
        product_grid = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item")))
        if not product_grid:
            self.fail("Product grid not loaded")

        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.product-item[data-productid='1'] button.product-box-add-to-cart-button")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found for the first product")
        add_to_cart_button.click()

        # Switch to the after_add_to_cart page
        driver.get('data:text/html;charset=utf-8,' + html_data["after_add_to_cart"])

        # Wait for the notification bar to appear
        notification = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.bar-notification.success")))
        if not notification:
            self.fail("Success notification not found")

        # Ensure the notification contains a link to the cart
        cart_link = notification.find_element(By.LINK_TEXT, "shopping cart")
        if not cart_link:
            self.fail("Shopping cart link not found in the notification")
        cart_link.click()

        # Load the cart page
        driver.get('data:text/html;charset=utf-8,' + html_data["cart_page"])

        # Verify that the cart contains at least one item
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.mini-shopping-cart .items .item")))
        if not cart_items:
            self.fail("No items found in the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()