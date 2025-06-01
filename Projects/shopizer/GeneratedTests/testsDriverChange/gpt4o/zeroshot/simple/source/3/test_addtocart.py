import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookies accept button not found")

        # Hover over the first product to reveal the "Add to cart" button
        try:
            product_element = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2")
            ))
            action_chains = ActionChains(driver)
            action_chains.move_to_element(product_element).perform()
        
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".product-wrap-2 .fa-shopping-cart")
            ))
            add_to_cart_button.click()
        except:
            self.fail("Failed to hover and add to cart")

        # Click the cart icon to open the cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".icon-cart")
            ))
            cart_icon.click()
        except:
            self.fail("Cart icon not found")

        # Confirm that the popup contains at least one item
        try:
            cart_items = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".single-shopping-cart")
            ))
            self.assertGreater(len(cart_items), 0, "Cart is empty")
        except:
            self.fail("Failed to confirm items in the cart popup")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()