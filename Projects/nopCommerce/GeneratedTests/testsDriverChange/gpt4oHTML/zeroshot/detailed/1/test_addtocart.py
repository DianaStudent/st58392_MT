import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Navigate to the homepage
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "master-wrapper-page")))

            # Click on "Search" from the main menu.
            search_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".top-menu.notmobile a[href='/search']"))
            )
            search_link.click()

            # Type the search term "book" into the search field.
            search_input = wait.until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            # Submit the search.
            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()

            # Wait for the product grid to load.
            product_grid = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )

            # Locate the first product result and click the "Add to cart" button.
            first_add_to_cart_button = product_grid.find_element(
                By.CSS_SELECTOR, ".product-item .product-box-add-to-cart-button")
            first_add_to_cart_button.click()

            # Wait for the notification bar to appear
            bar_notification = wait.until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            notification_text = bar_notification.find_element(By.CLASS_NAME, "content")
            self.assertIn("The product has been added to your", notification_text.text)

            # Click the "shopping cart" link from the notification.
            cart_link = notification_text.find_element(By.TAG_NAME, "a")
            cart_link.click()

            # Verify that the expected product is present in the cart page.
            cart_page = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-page"))
            )
            cart_items = driver.find_elements(By.CLASS_NAME, "item")
            self.assertTrue(cart_items, "Cart is empty")

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()