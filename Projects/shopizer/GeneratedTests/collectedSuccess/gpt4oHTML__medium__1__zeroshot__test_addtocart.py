import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Use the appropriate URL for the home page
        self.driver.set_window_size(1280, 1024)  # Adjusting the window size as needed

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Accept Cookies
        try:
            accept_cookies_btn = wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button')))
            accept_cookies_btn.click()
        except Exception:
            self.fail("Accept cookies button not found")

        # Step 2: Hover over a product image to reveal the "Add to cart" button
        try:
            product_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-child(1) .product-img"))
            )
            ActionChains(driver).move_to_element(product_element).perform()

            # Finding and clicking the "Add to cart" button within the product action context
            add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-child(1) .fa-shopping-cart"))
            )
            add_to_cart_button.click()
        except Exception:
            self.fail("Failed to hover and click on 'Add to cart' button")

        # Step 3: Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
            cart_icon.click()
        except Exception:
            self.fail("Failed to open the cart popup")

        # Step 4: Verify that at least one product is listed in the popup cart
        try:
            cart_popup = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
            )
            cart_items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertGreater(len(cart_items), 0, "Cart popup is empty, no items found")
        except Exception:
            self.fail("Failed to verify the presence of items in the cart popup")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()