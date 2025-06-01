from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        try:
            product_wrap = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
            )
            action = ActionChains(driver)
            action.move_to_element(product_wrap).perform()
        except:
            self.fail("Could not find product wrap element.")

        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button.")

        # Hover over the second product to reveal the "Add to cart" button
        try:
            product_wraps = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            product_wrap = product_wraps[1]
            action = ActionChains(driver)
            action.move_to_element(product_wrap).perform()
        except:
            self.fail("Could not find product wrap element.")

        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button.")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Could not find or click the cart icon.")

        # Confirm that the popup contains at least one item
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "single-shopping-cart"))
            )
        except:
            self.fail("Cart popup does not contain any items.")

if __name__ == "__main__":
    unittest.main()