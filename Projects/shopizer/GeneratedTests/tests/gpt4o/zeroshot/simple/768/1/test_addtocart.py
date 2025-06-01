import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception:
            self.fail("Failed to find or click the accept cookies button")

        # Hover over the first product and click 'Add to cart'
        try:
            first_product = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
            ActionChains(driver).move_to_element(first_product).click(add_to_cart_button).perform()
        except Exception:
            self.fail("Failed to hover over a product or click 'Add to cart'")

        # Click the cart icon to open the cart popup
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except Exception:
            self.fail("Failed to find or click the cart icon")

        # Verify that the cart popup contains at least one item
        try:
            cart_popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
            items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertGreater(len(items), 0, "The cart popup does not contain any items")
        except Exception:
            self.fail("Failed to verify the items in the cart popup")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()