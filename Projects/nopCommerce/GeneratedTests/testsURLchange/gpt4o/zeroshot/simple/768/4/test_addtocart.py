import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://max/")
        self.driver.set_window_size(1920, 1080)

    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Wait for the search box to be present and input search terms
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_box.send_keys(Keys.RETURN)

            # Wait for the search button to be present and click it if necessary
            # (Could be omitted since 'RETURN' submits, but explicit click might be needed)
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
            )
            search_button.click()

            # Wait for the search results to be visible and click "Add to cart" for the first product
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()

            # Wait for the "product added" notification to appear
            notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )

            # Check if the notification contains a link to the cart
            cart_link_present = notification.find_element(By.CSS_SELECTOR, "a[href='/cart']")
            self.assertIsNotNone(cart_link_present, "Cart link not found in success notification")

            # Go to cart and confirm at least one item is present
            cart_link_present.click()
            
            # Wait for the cart page to load and validate the cart contains at least one item
            cart_item_count = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".count a"), "1 item(s)")
            )

            if not cart_item_count:
                self.fail("Cart does not contain the expected number of items.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()