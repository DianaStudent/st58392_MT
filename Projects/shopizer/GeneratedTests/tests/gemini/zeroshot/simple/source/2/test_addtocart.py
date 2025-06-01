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

            add_to_cart_button = product_wrap.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            ActionChains(driver).move_to_element(product_wrap).perform()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button)).click()

        except Exception as e:
            self.fail(f"Could not add product to cart: {e}")

        # Hover over the second product to reveal the "Add to cart" button
        try:
            product_wraps = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            product_wrap = product_wraps[1]

            add_to_cart_button = product_wrap.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            ActionChains(driver).move_to_element(product_wrap).perform()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button)).click()

        except Exception as e:
            self.fail(f"Could not add product to cart: {e}")

        # Open the cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Could not open cart popup: {e}")

        # Confirm that the popup contains at least one item
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
            )
            cart_items = driver.find_elements(By.CLASS_NAME, "single-shopping-cart")
            self.assertTrue(len(cart_items) >= 1, "Cart popup does not contain any items.")
        except Exception as e:
            self.fail(f"Could not validate cart popup content: {e}")

if __name__ == "__main__":
    unittest.main()