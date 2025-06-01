import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # update with your correct URL
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the button is available
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception:
            self.fail("Accept cookies button not found or not clickable.")

        # Hover over the first product item to reveal the "Add to cart" button
        try:
            first_product = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2.mb-25"))
            )
            actions.move_to_element(first_product).perform()

            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception:
            self.fail("Failed to hover over product or find 'Add to Cart' button.")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_icon.click()
        except Exception:
            self.fail("Failed to find or click the cart icon.")

        # Confirm success by checking that the popup contains at least one item
        try:
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active .single-shopping-cart"))
            )
        except Exception:
            self.fail("Shopping cart popup does not contain any items.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()