from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable.")

        # Hover over the product item to reveal the "Add to cart" button
        try:
            product_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(product_item).perform()
        except:
            self.fail("Product item not found.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("'Add to cart' button not found or not clickable.")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable.")

        # Confirm success by checking that the popup contains at least one item
        try:
            shopping_cart_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
            items_in_cart = shopping_cart_content.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertGreater(len(items_in_cart), 0, "Cart does not contain any items.")
        except:
            self.fail("Shopping cart popup not found or does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()