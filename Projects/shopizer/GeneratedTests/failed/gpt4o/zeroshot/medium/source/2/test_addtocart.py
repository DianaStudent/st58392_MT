from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Cookie accept button not found or not clickable.")

        # Hover over the first product to reveal "Add to cart" button
        try:
            first_product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
            ActionChains(driver).move_to_element(first_product_image).perform()
        except:
            self.fail("First product image not found or not hoverable.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-wrap-2 .fa-shopping-cart")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable.")

        # Click on cart icon to open cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable.")

        # Verify that at least one product is listed in the popup cart
        try:
            cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".single-shopping-cart")))
            self.assertGreater(len(cart_items), 0, "No items in cart popup.")
        except:
            self.fail("Cart popup items not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()