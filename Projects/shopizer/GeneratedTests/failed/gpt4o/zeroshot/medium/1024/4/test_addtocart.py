from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookie consent if exists
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            if accept_button:
                accept_button.click()
        except:
            self.fail("Cookie consent button not found")

        # Hover over product to reveal "Add to cart" button
        try:
            product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
            ActionChains(driver).move_to_element(product).perform()
        except:
            self.fail("Product image not found to hover")

        # Click "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 > button[title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Click on cart icon to open cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found to open cart popup")

        # Verify at least one product is listed in the cart popup
        try:
            cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".single-shopping-cart")))
            self.assertGreater(len(cart_items), 0, "No items found in cart popup")
        except:
            self.fail("Cart popup did not open or no items found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()