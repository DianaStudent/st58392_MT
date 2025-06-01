from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Accept cookies
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()

            # Hover over a product to reveal the "Add to cart" button
            product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-child(1) .product-img"))
            )
            ActionChains(driver).move_to_element(product).perform()

            # Click the "Add to cart" button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-child(1) .fa-shopping-cart"))
            )
            add_to_cart_button.click()

            # Click the cart icon to open the cart popup
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .icon-cart"))
            )
            cart_icon.click()

            # Verify that at least one product is listed in the popup cart
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".single-shopping-cart"))
            )
            if len(cart_items) == 0:
                self.fail("No product found in the cart popup.")

        except Exception as e:
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()