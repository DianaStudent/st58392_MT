from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept Cookies
        try:
            accept_cookies_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button is missing or not clickable: {str(e)}")

        # Hover over first product to reveal "Add to cart" button
        try:
            first_product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:first-child .product-img"))
            )
            ActionChains(driver).move_to_element(first_product).perform()
        except Exception as e:
            self.fail(f"First product is missing or not hoverable: {str(e)}")

        # Click on the "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:first-child .fa-shopping-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"'Add to cart' button is missing or not clickable: {str(e)}")

        # Click on the cart icon to open the cart popup
        try:
            cart_icon = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon is missing or not clickable: {str(e)}")

        # Verify that at least one product is listed in the popup cart
        try:
            popup_cart_items = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".shopping-cart-content.active .single-shopping-cart"))
            )
            self.assertGreater(len(popup_cart_items), 0, "No items in the popup cart.")
        except Exception as e:
            self.fail(f"Popup cart items are missing or not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()