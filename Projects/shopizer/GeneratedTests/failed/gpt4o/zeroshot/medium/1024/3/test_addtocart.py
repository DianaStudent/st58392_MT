from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Cookie consent button not found or not clickable.")

        # Hover over a product image to reveal "Add to cart" button
        try:
            product_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(product_element).perform()
        except:
            self.fail("Product element not found or not visible.")

        # Click on "Add to cart" button
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable.")

        # Click on cart icon to open cart popup
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable.")

        # Verify cart popup has at least one item
        try:
            cart_content = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content ul")))
            items = cart_content.find_elements(By.TAG_NAME, "li")
            self.assertTrue(len(items) > 0, "No items in cart popup.")
        except:
            self.fail("Cart popup or items not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()